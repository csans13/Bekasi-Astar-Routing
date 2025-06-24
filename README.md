# Bekasi-Astar-Routing

**Perencanaan Jalur Transportasi Umum Kota Bekasi berbasis Algoritma A\***

---

## Deskripsi

**Bekasi-Astar-Routing** mengimplementasikan perencanaan rute transportasi umum di Kota Bekasi dengan memanfaatkan algoritma A\*. Program ini membangun model jaringan jalan menggunakan data OpenStreetMap (OSM) yang diproses melalui pustaka OSMnx dan NetworkX. Pengguna dapat menentukan dua titik strategis sebagai asal dan tujuan perjalanan, lalu sistem akan merekomendasikan jalur terpendek yang mengikuti ruas jalan, lengkap dengan visualisasi interaktif berbasis Folium.

---

## Fitur

* Pemetaan otomatis jaringan jalan Kota Bekasi dari OpenStreetMap
* Pilihan titik asal dan tujuan berdasarkan koordinat atau nama strategis (terminal, stasiun, kawasan permukiman, dll.)
* Pencarian rute optimal menggunakan algoritma A\* pada graf berbobot
* Visualisasi hasil rute secara interaktif pada peta HTML (Folium)
* Struktur program modular dan mudah dikembangkan

---

## Struktur Direktori

```
bekasi-astar-routing/
├── config.py
├── data.py
├── graph_utils.py
├── astar_solver.py
├── visualisasi.py
├── main.py
├── requirements.txt
├── README.md
```

---

## Instalasi

1. **Clone repository ini:**

   ```bash
   git clone https://github.com/yourusername/bekasi-astar-routing.git
   cd bekasi-astar-routing
   ```
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Cara Menjalankan

1. **Atur titik asal dan tujuan** di `config.py` dengan memilih dari `data.py` atau memasukkan koordinat sendiri.
2. **Jalankan program utama:**

   ```bash
   python main.py
   ```
3. **Lihat hasil rute dan peta:**

   * Output terminal akan menampilkan urutan node serta jumlah segmen yang ditempuh.
   * File HTML hasil visualisasi rute dapat dibuka di browser untuk melihat peta interaktif.

---

## Contoh Kasus Uji

Empat pengujian utama yang telah diimplementasikan:

* Pasar Bantar Gebang ke Harapan Indah
* Kawasan Kranggan ke Pondok Ungu Permai
* Komsen Jatiasih ke Summarecon Bekasi
* Perumahan Vida ke Pasar Sumber Arta

---

**Dikembangkan untuk kebutuhan riset dan edukasi transportasi umum Kota Bekasi.**
