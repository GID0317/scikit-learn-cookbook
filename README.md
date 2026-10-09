# scikit-learn Cookbook

Reproduksi kode, penjelasan teori, dan pembahasan hasil Chapter 1–8 buku **scikit-learn Cookbook, Third Edition: Over 80 recipes for machine learning in Python with scikit-learn**, John Sukup (Packt, 2025), ISBN 978-1-83664-445-3.

## Identitas

| Keterangan | Isi |
| --- | --- |
| Nama | GHAVIND AZZARYA |
| NIM | 101032300012 |
| Kelas | TK-47-03 |
| Mata kuliah | PEMBELAJARAN MESIN |

## Pengumpulan Tugas 2

Setiap bab mempunyai satu notebook yang memuat kode, teori dalam bahasa Indonesia, output eksekusi, latihan yang sudah diselesaikan, dan ringkasan hasil. Cakupan mengikuti dua tahap yang memiliki deadline pada dokumen tugas:

| Tahap | Cakupan | Deadline |
| --- | --- |
| 1 | Chapter 1–5 | 10 Oktober 2026, 23.59 |
| 2 | Chapter 6–8 | 17 Oktober 2026, 23.59 |

Dokumen tugas menyebut O’Reilly; buku pada tautan yang diberikan adalah edisi ketiga terbitan Packt yang juga tersedia melalui platform O’Reilly. Edisi buku dan repo kode penerbit telah dicocokkan. Buku memiliki Chapter 9–13; repo ini berfokus pada Chapter 1–8 sesuai dua tahap deadline tersebut.

## Notebook dan Ringkasan Bab

| Bab | Notebook | Pokok pembahasan |
| --- | --- | --- |
| 1 | [Common Conventions and API Elements of scikit-learn](notebooks/chapter_01_common_conventions_and_api_elements_of_scikit_learn.ipynb) | Estimator, transformer, pipeline, custom API, tuning, metadata. |
| 2 | [Pre-Model Workflow and Data Preprocessing](notebooks/chapter_02_pre_model_workflow_and_data_preprocessing.ipynb) | Missing data, scaling, encoding, feature engineering, pipeline. |
| 3 | [Dimensionality Reduction Techniques](notebooks/chapter_03_dimensionality_reduction_techniques.ipynb) | PCA, LDA, t-SNE, pemilihan metode dan validasi. |
| 4 | [Building Models with Distance Metrics and Nearest Neighbors](notebooks/chapter_04_building_models_with_distance_metrics_and_nearest_neighbors.ipynb) | KNN, metrik jarak, tuning, learning curve dan evaluasi. |
| 5 | [Linear Models and Regularization](notebooks/chapter_05_linear_models_and_regularization.ipynb) | OLS, Ridge, Lasso, ElasticNet, polynomial dan spline. |
| 6 | [Advanced Logistic Regression and Extensions](notebooks/chapter_06_advanced_logistic_regression_and_extensions.ipynb) | Binary/multiclass/multilabel, regularisasi, metrik klasifikasi. |
| 7 | [Support Vector Machines and Kernel Methods](notebooks/chapter_07_support_vector_machines_and_kernel_methods.ipynb) | Margin, kernel, SVC/SVR, tuning dan dimensi tinggi. |
| 8 | [Tree-Based Algorithms and Ensemble Methods](notebooks/chapter_08_tree_based_algorithms_and_ensemble_methods.ipynb) | Decision tree, random forest, boosting, stacking dan tuning. |

Pemetaan topik dan halaman buku tersedia pada [Cakupan Materi](docs/CAKUPAN_MATERI.md). Asal tiap sel kode tercatat dalam [CODE_SOURCES.json](docs/CODE_SOURCES.json).

### Chapter 1: Common Conventions and API Elements of scikit-learn

API estimator, transformer, dan pipeline memberi pola fit–transform–predict yang konsisten. Bab ini mereproduksi regresi lima titik, KMeans, scaling, atribut model, dan konfigurasi hyperparameter, lalu menambahkan custom transformer serta metadata routing. Statistik preprocessing dipelajari dari training dan dipakai kembali pada data baru.

### Chapter 2: Pre-Model Workflow and Data Preprocessing

Preprocessing menangani missing value, perbedaan skala, kategori, dan pembentukan fitur. SimpleImputer, KNNImputer, dan IterativeImputer dibandingkan; scaling, encoding, RFE, serta SelectFromModel ditunjukkan. Latihan akhir memakai California Housing dan pipeline random forest dengan target yang jelas serta split sebelum preprocessing.

### Chapter 3: Dimensionality Reduction Techniques

PCA menjaga varians tanpa label, LDA memakai label untuk separabilitas, dan t-SNE menjaga kedekatan lokal untuk visualisasi. Wine dan Digits menunjukkan perbedaan tujuan ketiga metode. Latihan membandingkan klasifikasi dengan/tanpa PCA dan warna label versus cluster pada proyeksi t-SNE; bentuk plot bukan ukuran accuracy.

### Chapter 4: Building Models with Distance Metrics and Nearest Neighbors

KNN mencari tetangga terdekat dan menggunakan voting atau rata-rata respons. Nilai k, bobot, scaling, serta metrik jarak memengaruhi hasil. Grid search, learning curve, confusion matrix, dan classification report digunakan untuk memahami generalisasi serta jenis kesalahan pada Iris dan contoh latihan.

### Chapter 5: Linear Models and Regularization

Regresi linear memodelkan respons numerik; Ridge, Lasso, dan ElasticNet mengendalikan kompleksitas melalui penalti. Coefficient path menunjukkan shrinkage, sedangkan polynomial dan spline menangkap bentuk nonlinier. Derajat polinomial dipilih dengan cross-validation training dan hasil test dibedakan dari training.

### Chapter 6: Advanced Logistic Regression and Extensions

Logistic regression menghasilkan probabilitas kelas melalui sigmoid atau softmax. Bab ini membandingkan OvR/multinomial, penalti L1/L2, serta klasifikasi multilabel. Precision, recall, F1, ROC-AUC, subset accuracy, dan Hamming loss menjawab pertanyaan berbeda; positive class pada Breast Cancer dijelaskan secara eksplisit.

### Chapter 7: Support Vector Machines and Kernel Methods

SVM mencari pemisah dengan margin lebar; kernel menangkap hubungan nonlinier tanpa membangun semua fitur secara eksplisit. C, gamma, degree, dan scaling dikaji melalui CV. Contoh SVR dengan nomor kelas dari buku diberi batas interpretasi, lalu dilengkapi target kontinu yang sesuai untuk evaluasi regresi.

### Chapter 8: Tree-Based Algorithms and Ensemble Methods

Decision tree membagi data secara rekursif; random forest menggabungkan pohon acak, gradient boosting membangun model bertahap, dan stacking memakai meta-model. Contoh Iris dilengkapi tuning serta latihan Wine, Breast Cancer, dan Digits. Feature importance dan skor satu split dijelaskan beserta batas interpretasinya.

## Menjalankan Notebook

Output tersimpan sehingga notebook dapat dibaca langsung di GitHub. Untuk menjalankan ulang, gunakan **Python 3.12** dan dependency yang dipin. Dari root repo pada PowerShell:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m ensurepip
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe scripts/verify_notebooks.py
```

Untuk menjalankan satu tahap:

```powershell
.venv/Scripts/python.exe scripts/verify_notebooks.py --chapter 1 2 3 4 5
.venv/Scripts/python.exe scripts/verify_notebooks.py --chapter 6 7 8
```

Untuk eksekusi interaktif, buka notebook di Jupyter atau VS Code, pilih Python dari `.venv`, lalu gunakan Restart Kernel dan Run All. Working directory dapat berupa root repo atau folder `notebooks`. Script verifikasi memilih interpreter yang menjalankannya secara eksplisit.

## Data dan Reproduksibilitas

Iris, Wine, Digits, dan Breast Cancer tersedia melalui loader bawaan scikit-learn. Data sintetis dibuat dengan seed tetap. California Housing disertakan sebagai array NPZ agar eksekusi tidak memerlukan jaringan; asal, unit target, dan SHA-256 dicatat pada [SOURCES.json](data/SOURCES.json). Checksum diverifikasi sebelum eksekusi notebook.

Lingkungan `.venv`, cache, file sementara, dan ZIP diabaikan Git. PDF buku dan dokumen tugas tidak dimasukkan ke repository. Versi langsung dependency dipin pada [requirements.txt](requirements.txt). Perbedaan platform dapat menghasilkan selisih numerik kecil.

<details>
<summary><strong>Adaptasi kode dan batas interpretasi</strong></summary>

Kode Chapter 2–8 diadaptasi dari repo penerbit pada commit `c624b1279cf23a83273e806cede15cad0c9e5500`, termasuk exercise solutions. Chapter 1 ditulis dari contoh buku karena notebook penerbit mulai Chapter 2. Penjelasan dan ringkasan disusun untuk repo ini.

- Semua sel latihan sumber sudah dilengkapi; seed ditetapkan untuk simulasi dan estimator yang memakai pengacakan.
- Chapter 2 memakai Salary sebagai target eksplisit pada contoh pipeline campuran. Split dilakukan sebelum preprocessing. LabelEncoder per kolom dipertahankan sebagai ilustrasi pemetaan, dengan penjelasan bahwa fitur nominal tidak memiliki urutan alami.
- Chapter 3 menghapus panah yang mengambil dua koefisien loading ruang 13 fitur lalu menempatkannya sebagai koordinat di ruang PCA 2D. Plot proyeksi dan explained variance tetap ditampilkan.
- Chapter 4 dan 7 memakai scaling di pipeline untuk tuning, sehingga statistik scaler dipelajari di dalam tiap fold. Minimum ukuran training learning curve dijaga agar tidak lebih kecil daripada jumlah tetangga.
- Chapter 5 memilih derajat polynomial melalui CV training. Kurva dan spline dilatih pada training; metrik test dipisahkan dari metrik training. Regresi spline tidak disebut interpolasi yang wajib melewati setiap titik.
- Chapter 6 memakai OvR eksplisit, scaling pada model binary yang relevan, positive class yang jelas, dan zero_division=0 pada contoh metrik. Multilabel dievaluasi dengan subset accuracy serta Hamming loss.
- Chapter 7 menjelaskan batas contoh SVR pada nomor kelas Iris, lalu menambahkan contoh respons kontinu. Accuracy evaluasi SVM dihitung dari prediksi model terkait, bukan variabel lama.
- Chapter 8 memperbaiki judul bab yang keliru pada sumber dan menampilkan heatmap pada satu learning rate terbaik dari CV.

Skor satu split bukan jaminan generalisasi pada distribusi, lokasi, atau waktu lain. Menggunakan beberapa model pada holdout untuk ilustrasi tidak sama dengan evaluasi final dari proses pemilihan model; nested CV atau test baru diperlukan untuk estimasi independen setelah pencarian berulang. Visualisasi eksploratif pada seluruh data diberi konteks dan tidak digunakan sebagai preprocessing bagi evaluasi test. Asosiasi dan feature importance bukan bukti kausal.

</details>

## Validasi

Hasil eksekusi, jumlah sel kode/grafik, serta pemeriksaan konsistensi tersedia pada [Laporan Validasi](docs/VALIDASI.md). Script berhenti jika ada error; output bukan berasal dari notebook mahasiswa lain.

## Referensi dan Lisensi

1. Sukup, J. (2025). *scikit-learn Cookbook*, Third Edition. Packt. ISBN 9781836644453.
2. [Kode penerbit](https://github.com/PacktPublishing/scikit-learn-Cookbook-Third-Edition), commit `c624b1279cf23a83273e806cede15cad0c9e5500`.
3. [Dokumentasi scikit-learn 1.5](https://scikit-learn.org/1.5/) dan [pencegahan data leakage](https://scikit-learn.org/1.5/common_pitfalls.html).
4. [Contoh pengumpulan dari dokumen tugas](https://github.com/farrelrassya/scikit-learn-cookbook). Digunakan sebagai pembanding struktur; kode utama berasal dari buku dan penerbit.

Lisensi MIT dari repo kode penerbit disertakan pada [LICENSE](LICENSE). Atribusi dan lisensi kode dipertahankan. Hak cipta buku tetap milik penerbit; PDF buku tidak didistribusikan dalam repo ini.
