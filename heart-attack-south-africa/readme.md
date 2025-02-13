# Analisis Prediksi Risiko Serangan Jantung

## 1. Pendahuluan
Dataset ini berisi faktor risiko serangan jantung pada individu di Afrika Selatan. Data ini mencakup detail demografis, riwayat medis, kebiasaan gaya hidup, dan pengukuran klinis untuk mengevaluasi kemungkinan serangan jantung. Analisis ini bertujuan untuk membangun model machine learning yang dapat memprediksi risiko serangan jantung berdasarkan fitur-fitur yang relevan.

## 2. Dataset
### Sumber Dataset:
[Heart Attack in Youth vs Adult in South Africa](https://www.kaggle.com/datasets/ashaychoudhary/heart-attack-in-youth-vs-adult-in-south-africa)

### Deskripsi Fitur:
- **Age**: Usia pasien dalam tahun.
- **Cholesterol_Level**: Kadar kolesterol dalam darah (mg/dL).
- **Blood_Pressure_Systolic & Diastolic**: Tekanan darah sistolik dan diastolik (mmHg).
- **Smoking_Status**: Status merokok (1 = Ya, 0 = Tidak).
- **Obesity_Index**: Indeks obesitas berdasarkan BMI.
- **Diabetes_Status**: Status diabetes (1 = Ya, 0 = Tidak).
- **Family_History_Heart_Disease**: Riwayat keluarga dengan penyakit jantung (1 = Ada, 0 = Tidak).
- **Triglycerides_Level**: Kadar trigliserida dalam darah (mg/dL).
- **Heart_Attack_Outcome**: Target klasifikasi (0 = Tidak, 1 = Ya).

## 3. Preprocessing Data
### 3.1 Data Cleaning & Understanding
- Menghapus data duplikat jika ada.
- Menangani nilai yang hilang (missing values).
- Mengeksplorasi distribusi data dan hubungan antar fitur menggunakan visualisasi.

### 3.2 Exploratory Data Analysis (EDA)
- Menangani outlier menggunakan IQR method.
- Memeriksa distribusi fitur menggunakan histogram dan boxplot.
- Mengecek korelasi antar fitur menggunakan heatmap korelasi.

### 3.3 Feature Engineering
- **Normalisasi (Min-Max Scaler)** untuk model yang sensitif terhadap skala data (contoh: SVM).
- **Feature Selection menggunakan Embedded Method**
  - Menggunakan **Random Forest** untuk menilai pentingnya fitur.
  - Memilih fitur dengan importance di atas median.
  - Hasil fitur terpilih:
    - Age
    - Cholesterol_Level
    - Blood_Pressure_Systolic
    - Blood_Pressure_Diastolic
    - Smoking_Status
    - Obesity_Index
    - Diabetes_Status
    - Family_History_Heart_Disease
    - Triglycerides_Level

## 4. Model Machine Learning
Berbagai model telah diuji dengan metrik evaluasi seperti **Accuracy, Precision, Recall, dan F1-Score**.

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| K-Nearest Neighbors (KNN) | 95.10% | 95.75% | 95.95% | 95.85% |
| Decision Tree (DT) | 99.98% | 99.97% | 99.99% | 99.98% |
| Random Forest (RF) | 92.61% | 90.31% | 97.96% | 93.98% |
| Support Vector Machine (SVM) | 87.23% | 88.52% | 89.98% | 89.24% |
| Naive Bayes (NB) | 81.70% | 83.31% | 86.21% | 84.73% |

## 5. Prediksi dengan Data Baru
### Contoh Data Baru:
```python
new_data = pd.DataFrame([{
    'Age': 60,
    'Cholesterol_Level': 220,
    'Blood_Pressure_Systolic': 130,
    'Blood_Pressure_Diastolic': 85,
    'Smoking_Status': 1,
    'Obesity_Index': 27,
    'Diabetes_Status': 0,
    'Family_History_Heart_Disease': 1,
    'Triglycerides_Level': 180
}])
```
Hasil Prediksi: **"Risiko Serangan Jantung: Ya"**

## 6. Kesimpulan
- Decision Tree memiliki akurasi tertinggi dan bisa dilihat bahwa tidak terjadi overfitting.
- Random Forest menawarkan keseimbangan terbaik antara akurasi dan generalisasi.
- Fitur yang dipilih sangat relevan untuk prediksi risiko serangan jantung.


---



