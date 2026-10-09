# Laporan Validasi

Pemeriksaan pada 9 Oktober 2026 memakai Python 3.12.14, scikit-learn 1.5.2, dan NLTK 3.9.2. Chapter 1–8 sudah dieksekusi dari kernel baru pada pemeriksaan sebelumnya; Chapter 9–13 dieksekusi dari kernel baru pada pelengkapan ini. Ringkasan numerik berasal dari output notebook masing-masing.

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
| 9 | 21 | 5 | 0 | 0 |
| 10 | 21 | 12 | 0 | 1 |
| 11 | 20 | 13 | 0 | 0 |
| 12 | 16 | 4 | 0 | 0 |
| 13 | 17 | 2 | 0 | 0 |

Total **221 sel kode** dan **74 grafik** tersimpan, tanpa output error. Chapter 10 memuat satu peringatan graf spectral embedding tidak sepenuhnya terhubung; penyebab dan batas interpretasinya dijelaskan di notebook. Peringatan tersebut tidak disembunyikan.

## Pemeriksaan yang Dilakukan

- SHA-256 California Housing dan enam resource NLTK sesuai manifest; unduhan NLTK dipin ke commit sumber.
- Semua notebook lolos schema nbformat; seluruh sel kode memiliki execution_count, sintaks valid, dan tidak mempunyai output error.
- Semua latihan akhir memiliki implementasi; placeholder sumber telah diganti. Tautan README, daftar isi notebook, dan cakupan materi diperiksa.
- Pemeriksaan Chapter 1–8 mencakup hasil regresi, imputasi, scaling, bentuk proyeksi/prediksi, pemisahan training/test, probabilitas kelas, confusion matrix, serta feature importance.
- Chapter 9 memastikan bentuk vocabulary training/test konsisten, semua kelas latihan tersedia pada kedua bagian, indeks terpisah, dan confusion matrix menjumlah seluruh 1.000 review test.
- Chapter 10 memeriksa rentang metrik, variance PCA, probabilitas GMM yang berjumlah satu, serta jumlah cluster/noise.
- Chapter 11 memakai skor anomali dengan arah benar untuk AUC, membedakan evaluasi training dari novelty holdout, serta memeriksa recall dan false-positive rate. LOF novelty hanya menerima data baru.
- Chapter 12 memakai pipeline dalam CV; split group tidak berbagi identitas dan split waktu menjaga training mendahului validation. Kurva latihan memakai training saja.
- Chapter 13 membandingkan prediksi sebelum/sesudah serialization, memakai versi runtime aktual, menyimpan snapshot validation terpisah, dan mencatat keputusan gate beserta skor serta threshold. Stream dievaluasi sebelum update.
- Sampel grafik Chapter 1–8 telah diperiksa sebelumnya. Sampel tambahan teks, clustering, anomali, kurva CV, dan monitoring deployment diperiksa secara visual pada pelengkapan ini.

## Batas Validasi

Assertion memeriksa konsistensi yang dinyatakan dalam kode, bukan seluruh asumsi statistik. Skor satu holdout acak tidak menjamin generalisasi ke wilayah, waktu, atau domain berbeda. Metric anomaly pada dataset tercemar training adalah evaluasi deskriptif dan tidak disebut test independen. Nomor cluster tidak identik dengan label kelas.

Notebook Chapter 13 mensimulasikan lifecycle lokal. Tidak ada service internet, registri produksi, atau SLA yang diuji. Seluruh grafik tidak diklaim diperiksa satu per satu; pemeriksaan visual memakai sampel. Eksekusi ulang membutuhkan dependency yang dipin dan persiapan resource NLTK sekali melalui internet.
