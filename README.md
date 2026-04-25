# 🚲 Bike Sharing Analytics Dashboard

Dashboard interaktif ini dikembangkan untuk menganalisis tren penyewaan sepeda menggunakan dataset "Bike Sharing". Proyek ini mengeksplorasi bagaimana dinamika waktu, tipe pengguna, dan kondisi cuaca memengaruhi volume penyewaan.

---

##  Profil Pengembang
* *Nama:* Nayza Azura Putri
* *Email:* nayzaabdi05@gmail.com
* *ID Dicoding:* CDCC220D6X1019
* *Instansi:* UIN Sultan Syarif Kasim Riau

---

## Project Struktur
- data/: Direktori yang berisi dataset mentah (day.csv & hour.csv).
- dashboard.py: File utama untuk menjalankan dashboard Streamlit.
- Notebook.ipynb: File dokumentasi proses analisis data (Data Wrangling, EDA, Visualisasi).
- requirements.txt: Daftar library Python yang digunakan.
- README.md: Dokumentasi proyek.

---
  
## Pertanyaan Analisis
1. *Pola Waktu:* Bagaimana perbedaan pola pengguna sepeda antara pengguna Casual dan Registered pada hari kerja dibandingkan hari libur selama tahun 2011-2012?
2. *Faktor Cuaca & Pemeliharaan:* Pada kondisi cuaca seperti apa jumlah penyewaan sepeda mengalami penurunan paling drastis, dan jam-jam berapa saja yang paling kritis untuk dilakukan pemeliharaan sepeda tanpa mengganggu layanan?

---

## Setup Environment

### 1. Install Python
Pastikan Python sudah terinstall di komputer Anda.

### 2. Install Library
Jalankan perintah berikut pada CMD / Terminal:

bash
pip install -r requirements.txt


---

## Menjalankan Dashboard

Masuk ke folder project:

bash
cd submission


Jalankan aplikasi Streamlit:

bash
python -m streamlit run dashboard.py


---
## Hasil Analisis Data
Pertanyaan 1: Berdasarkan analisis data, terdapat perbedaan pola yang signifikan antara hari kerja dan hari libur. Pada hari kerja (working day), puncak penyewaan terjadi pada jam berangkat dan pulang kantor, yaitu pukul 08.00 (rata-rata 477.03 sewa) dan pukul 17.00 (rata-rata 461.14 sewa). Sementara itu, pada hari libur (holiday/weekend), pola penyewaan lebih terfokus di siang hari dengan puncak pada pukul 13.00 (rata-rata 385.37 sewa). Hal ini menunjukkan bahwa pada hari kerja sepeda digunakan sebagai alat transportasi komuter, sedangkan pada hari libur digunakan untuk rekreasi.

Pertanyaan 2: Kondisi cuaca memiliki dampak besar terhadap jumlah penyewaan sepeda. Rata-rata penyewaan tertinggi terjadi pada kondisi cuaca cerah (Clear/Partly Cloudy) dengan rata-rata 4.876,7 sewa per hari. Sebaliknya, pada kondisi cuaca hujan atau salju ringan (Light Rain/Snow), penyewaan turun drastis hingga sekitar 63% menjadi hanya 1.803,2 sewa per hari. Selain itu, analisis korelasi menunjukkan bahwa suhu (temp) memiliki hubungan positif yang kuat (0.63) terhadap jumlah penyewaan, yang berarti semakin hangat suhu, semakin tinggi minat masyarakat untuk menyewa sepeda.
