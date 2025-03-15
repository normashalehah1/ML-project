# Prediksi Anak Berkebutuhan Khusus dengan KNN

## Deskripsi Proyek
Proyek ini bertujuan memenuhi tugas untuk mata kuliah kecerdasan buatan yang berfokus memprediksi kategori kebutuhan khusus anak berdasarkan beberapa fitur menggunakan algoritma **K-Nearest Neighbors (KNN)**. Model ini dibangun menggunakan dataset yang berisi informasi tentang durasi fokus, respon suara, dan aktivitas fisik anak, serta rekomendasi kegiatan yang sesuai.

## Dataset
Dataset yang digunakan memiliki fitur-fitur berikut:
- `Durasi_Fokus_menit` : Durasi fokus anak dalam hitungan menit.
- `Respon_Suara` : Respon anak terhadap suara (misalnya: Sedang, Cepat).
- `Aktivitas_Fisik` : Aktivitas fisik anak (Diam/Bergerak).
- `Kategori` : Kategori kebutuhan khusus anak (Kesulitan Fokus, Sensitivitas Suara, dll.).
- `Rekomendasi_Kegiatan` : Rekomendasi aktivitas yang sesuai.

## Metode
Proyek ini menerapkan beberapa tahapan utama:
1. **Data Cleaning**: Membersihkan data dari missing values atau data yang tidak relevan.
2. **Exploratory Data Analysis (EDA)**: Menganalisis distribusi data dan hubungan antar fitur.
3. **Training & Testing Data**: Membagi data menjadi set pelatihan dan pengujian.
4. **Implementasi KNN**: Menerapkan algoritma K-Nearest Neighbors untuk melakukan prediksi kategori kebutuhan khusus anak.

## Hasil
Model ini mampu memberikan prediksi kategori kebutuhan khusus anak berdasarkan input fitur yang diberikan. Hasil prediksi dapat digunakan untuk memberikan rekomendasi aktivitas yang sesuai bagi anak berkebutuhan khusus.

