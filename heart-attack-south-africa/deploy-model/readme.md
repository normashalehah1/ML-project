# Prediksi Penyakit Jantung dengan Decision Tree

Repository ini berisi aplikasi web sederhana untuk memprediksi penyakit jantung menggunakan model Decision Tree. Aplikasi ini dibangun dengan Flask sebagai backend dan HTML/CSS (dengan Bootstrap) sebagai frontend.

## Fitur
- Input data pasien melalui form HTML.
- Menggunakan model Decision Tree yang telah di-train untuk melakukan prediksi.
- Hasil prediksi ditampilkan sebagai "Ya" (penyakit jantung) atau "Tidak" (tidak ada penyakit jantung).

## Struktur Folder
/prediksi_jantung
│── /templates
│   └── index.html       # File frontend HTML
│── /static
│   └── style.css        # File styling (optional)
│── decision_tree_model.pkl  # File model yang telah di-train
│── app.py               # File aplikasi Flask
│── requirements.txt     # Daftar library yang diperlukan
│── README.md            # Dokumentasi proyek

## Cara Install dan Menjalankan Aplikasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/nama-repo.git
   cd nama-repo
2. **Buat Virtual Environment**
   ```
   python -m venv venv
   source venv/bin/activate  # Untuk Mac/Linux
   venv\Scripts\activate     # Untuk Windows

3. 
