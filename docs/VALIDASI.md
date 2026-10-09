# Laporan Validasi

Pemeriksaan pada 9 Oktober 2026 memakai Python 3.12.14 dan scikit-learn 1.5.2. Setiap notebook dijalankan dari kernel baru menggunakan dependency pada requirements.txt. Angka pada ringkasan diambil dari output notebook yang sama.

| Chapter | Sel kode | Grafik PNG | Output error | Peringatan dalam notebook |
| --- | --- | --- | --- | --- |
| 1 | 9 | 0 | 0 | 0 |
| 2 | 21 | 0 | 0 | 0 |
| 3 | 12 | 7 | 0 | 0 |
| 4 | 12 | 3 | 0 | 0 |
| 5 | 12 | 10 | 0 | 0 |
| 6 | 18 | 7 | 0 | 0 |
| 7 | 23 | 7 | 0 | 0 |
| 8 | 19 | 4 | 0 | 0 |

Total **126 sel kode** dan **38 grafik** tersimpan, tanpa error notebook.

## Pemeriksaan yang Dilakukan

- Checksum California Housing sama dengan manifest sumber.
- Notebook lolos schema nbformat; semua sel kode memiliki execution_count dan tidak memuat output error.
- Sintaks seluruh sel kode valid; placeholder sumber YOUR CODE HERE telah diganti implementasi selesai.
- Daftar isi serta tautan cakupan materi mengarah ke heading notebook yang tersedia.
- Contoh regresi Chapter 1 cocok dengan prediksi 5,75 dan 6,70; scaling dan custom transformer memenuhi pemeriksaan mean.
- Imputasi menghasilkan nilai finite; scaling memenuhi pemeriksaan mean; indeks California training/test terpisah.
- Bentuk proyeksi PCA/LDA/t-SNE sesuai dataset, varians PCA berada pada rentang 0–1, dan preprocessing evaluasi Digits belajar dari training.
- Confusion matrix KNN mempunyai jumlah sampel yang benar; scaler berada di pipeline tuning.
- Derajat polynomial dipilih pada CV training; prediksi test mempunyai jumlah baris yang benar.
- Bentuk prediksi multilabel sesuai target; probabilitas multinomial berjumlah satu per baris.
- Contoh target kontinu SVR menghasilkan RMSE finite dan nonnegatif; evaluasi SVM menggunakan pipeline scaling.
- Feature importance forest berjumlah satu; accuracy ensemble berada pada rentang 0–1.
- Sampel grafik PCA/t-SNE, learning curve, confusion matrix, polynomial/residual, logistic regression, SVM, dan tree diperiksa secara visual.

## Batas Validasi

Assertion memeriksa konsistensi yang dinyatakan dalam kode, bukan seluruh asumsi statistik. Skor holdout acak tidak menjamin generalisasi pada transaksi masa depan, wilayah baru, atau populasi berbeda. Proyeksi eksploratif pada seluruh data tidak dipakai sebagai preprocessing untuk evaluasi test. Perbandingan model pada satu split dipakai untuk pembelajaran, bukan klaim optimum global.

Ringkasan teknis ini tidak mengklaim seluruh gambar telah diperiksa satu per satu atau bahwa model siap deployment. Untuk penggunaan nyata diperlukan desain evaluasi sesuai tujuan, pemeriksaan bias data, dan monitoring perubahan distribusi.
