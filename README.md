# Bekasi-Astar-Routing

**Perencanaan Jalur Transportasi Umum Kota Bekasi berbasis Algoritma A\*** 🚍🌐

---

## 📝 Deskripsi

**Bekasi-Astar-Routing** adalah mengimplementasikan perencanaan rute transportasi umum di Kota Bekasi dengan memanfaatkan algoritma A\*. Program ini membangun model jaringan jalan menggunakan data OpenStreetMap (OSM) yang diproses melalui pustaka OSMnx dan NetworkX. Pengguna dapat menentukan dua titik strategis sebagai asal dan tujuan perjalanan, lalu sistem akan merekomendasikan jalur terpendek yang mengikuti ruas jalan, lengkap dengan visualisasi interaktif berbasis Folium.

---

## ✨ Fitur

* Pemetaan otomatis jaringan jalan Kota Bekasi dari OpenStreetMap
* Pilihan titik asal dan tujuan berdasarkan koordinat atau nama strategis (terminal, stasiun, kawasan permukiman, dll.)
* Pencarian rute optimal menggunakan algoritma A\* pada graf berbobot
* Visualisasi hasil rute secara interaktif pada peta HTML (Folium)
* Struktur program modular dan mudah dikembangkan

---

## 📁 Struktur Direktori

```
bekasi-astar-routing/
├── doc/                         # Makalah
├── src/                         # Kode sumber utama
│   ├── __pycache__/             # File .pyc hasil kompilasi Python agar program berjalan lebih cepat
│   ├── cache/                   # Cache OSMnx untuk mempercepat scraping peta
│   ├── astar_solver.py
│   ├── config.py
│   ├── data.py
│   ├── graph_utils.py
│   ├── main.py
│   └── visualisasi.py
├── test/                        # Hasil pengujian
│   ├── Kawasan Kranggan ke Pondok Ungu Permai.html
│   ├── Komsen Jatiasih ke Summarecon Bekasi.html
│   ├── Pasar Bantar Gebang ke Harapan Indah.html
│   └── Perumahan Vida ke Pasar Sumber Arta.html
├── README.md
└── requirements.txt
```

---

## ⚡ Instalasi

1. **Clone repository ini:**

   ```bash
   git clone https://github.com/csans13/bekasi-astar-routing.git
   cd bekasi-astar-routing
   ```
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Cara Menjalankan

1. **Atur titik asal dan tujuan** di `src/config.py` dengan memilih dari `src/data.py` atau memasukkan koordinat sendiri.
2. **Jalankan program utama dari direktori src:**

   ```bash
   cd src
   python main.py
   ```
3. **Lihat hasil rute dan peta:**

   * Output terminal akan menampilkan urutan node serta jumlah segmen yang ditempuh.
   * File HTML hasil visualisasi rute dapat dibuka di browser untuk melihat peta interaktif.

---

## 🧪 Contoh Kasus Uji

Empat pengujian utama yang telah diimplementasikan (hasil peta tersedia di folder `/test`):

* Pasar Bantar Gebang ke Harapan Indah
* Kawasan Kranggan ke Pondok Ungu Permai
* Komsen Jatiasih ke Summarecon Bekasi
* Perumahan Vida ke Pasar Sumber Arta

---

> **Dikembangkan untuk kebutuhan riset dan edukasi transportasi umum Kota Bekasi.** 🚦🗺️
