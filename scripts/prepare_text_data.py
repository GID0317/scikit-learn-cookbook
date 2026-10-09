"""Fetch the pinned NLTK resources used by Chapter 9 into the project cache."""
from pathlib import Path
import hashlib
import json
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / '.cache/nltk_data'


def main():
    manifest = json.loads((ROOT / 'data/TEXT_SOURCES.json').read_text(encoding='utf-8'))
    for item in manifest['packages']:
        archive = DEST / item['path']
        archive.parent.mkdir(parents=True, exist_ok=True)
        if not archive.exists():
            print(f"Downloading {item['name']}", flush=True)
            urllib.request.urlretrieve(item['url'], archive)
        if hashlib.sha256(archive.read_bytes()).hexdigest() != item['sha256']:
            raise ValueError(f"Checksum mismatch: {archive}. Remove this archive and retry.")
        with zipfile.ZipFile(archive) as z:
            for member in z.namelist():
                target = (archive.parent / member).resolve()
                if not target.is_relative_to(archive.parent.resolve()):
                    raise ValueError(f'Unsafe archive member: {member}')
            z.extractall(archive.parent)
        print(f"READY {item['name']}: checksum verified", flush=True)
    print(f'NLTK resources ready in {DEST}')


if __name__ == '__main__':
    main()
