"""Execute selected chapter notebooks and validate local data before execution."""
from pathlib import Path
import argparse
import asyncio
import hashlib
import json
import os
import sys
import tempfile

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]


def main():
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    parser = argparse.ArgumentParser()
    parser.add_argument('--chapter', type=int, nargs='+', choices=range(1, 9))
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'data/SOURCES.json').read_text(encoding='utf-8'))
    dataset = ROOT / 'data' / manifest['filename']
    digest = hashlib.sha256(dataset.read_bytes()).hexdigest()
    if digest != manifest['sha256']:
        raise ValueError('California Housing checksum does not match SOURCES.json')

    # The explicit executable prevents accidental execution in another Python env.
    runtime = ROOT / 'tmp/jupyter'
    runtime.mkdir(parents=True, exist_ok=True)
    os.environ['JUPYTER_RUNTIME_DIR'] = str(runtime)
    os.environ['MPLCONFIGDIR'] = str(ROOT / '.cache/matplotlib')
    os.environ['IPYTHONDIR'] = str(ROOT / '.cache/ipython')
    os.environ['OMP_NUM_THREADS'] = '1'
    os.environ['OPENBLAS_NUM_THREADS'] = '1'
    os.environ['MKL_NUM_THREADS'] = '1'
    chapters = args.chapter or list(range(1, 9))
    report = []
    with tempfile.TemporaryDirectory(dir=runtime) as kernel_dir:
        spec_dir = Path(kernel_dir) / 'kernels/assignment'
        spec_dir.mkdir(parents=True)
        (spec_dir / 'kernel.json').write_text(json.dumps({
            'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
            'display_name': 'Assignment Python', 'language': 'python',
        }), encoding='utf-8')
        os.environ['JUPYTER_PATH'] = kernel_dir
        for chapter in chapters:
            path = next((ROOT / 'notebooks').glob(f'chapter_{chapter:02d}_*.ipynb'))
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
            print(f'Executing Chapter {chapter}: {path.name}', flush=True)
            client = NotebookClient(notebook, timeout=1200, kernel_name='assignment',
                                    resources={'metadata': {'path': str(ROOT)}})
            client.execute()
            nbformat.validate(notebook)
            errors = [output for cell in notebook.cells if cell.cell_type == 'code'
                      for output in cell.outputs if output.output_type == 'error']
            if errors:
                raise RuntimeError(f'Chapter {chapter} contains execution errors')
            nbformat.write(notebook, path)
            count = sum(c.cell_type == 'code' for c in notebook.cells)
            figures = sum('image/png' in o.get('data', {})
                          for c in notebook.cells if c.cell_type == 'code' for o in c.outputs)
            report.append({'chapter': chapter, 'code_cells': count, 'figures': figures})
            print(f'PASS Chapter {chapter}: {count} code cells, {figures} figures', flush=True)
    (ROOT / 'tmp/last_execution.json').write_text(json.dumps(report, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
