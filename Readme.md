# 📡 Network Monitoring Dashboard  
Tugas Mata Kuliah: **Komunikasi Data**  
Nama: **Rifaldi Ahmad Rehan**
NIM: **241091900397**

Aplikasi ini adalah sistem **Web Monitoring Jaringan secara real-time** untuk menganalisis status perangkat jaringan. Data diambil melalui **simulasi perangkat** yang mewakili metode ICMP/SNMP.

Aplikasi berjalan berbasis **Flask + Socket.IO** (Python) untuk memberikan update real-time melalui WebSocket, serta REST API untuk mengambil data historis.

---

# 1. Fitur Utama

### ✔ Monitoring Realtime (WebSocket)
- Status device (online/offline) diperbarui setiap 2 detik.
- Bandwidth tiap perangkat berubah secara real-time.
- Log aktivitas otomatis ditampilkan.

### ✔ Tiga Perangkat Jaringan (Disimulasikan)
- Router A  
- Switch B  
- Server C  

### ✔ REST API
- Endpoint untuk mengambil data historis perangkat dalam format JSON.

### ✔ Dashboard UI
- Menggunakan TailwindCSS
- Grafik bandwidth real-time dengan Chart.js
- Tabel status dinamis

---

# 2. Struktur Folder

```
network-monitoring-dashboard/
│
├── app.py
├── devices.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    |   └── main.js
    └── img/
        ├── chart_update.png
        ├── dashboard.png
        └── table_update.png
```

---

# 3. Instalasi

Pastikan Python 3 sudah terinstall.

### Install dependencies
Jalankan:

```
pip install -r requirements.txt
```

Atau manual:

```
pip install flask flask-socketio eventlet
```

---

# 4. Cara Menjalankan Aplikasi

Di terminal:

```
python app.py
```

Jika berhasil, server akan berjalan di:

```
http://localhost:5000
```

Buka browser untuk melihat dashboard realtime.

---

# 5. Endpoint REST API

### **GET /api/history**
Mengembalikan riwayat status perangkat dalam format JSON.

Contoh:

```json
[
  {
    "time": "2025-12-04T19:20:54",
    "data": [
      {"name": "Router A", "status": "online", "bandwidth": 12},
      {"name": "Switch B", "status": "offline", "bandwidth": 0},
      {"name": "Server C", "status": "online", "bandwidth": 25}
    ]
  }
]
```

---

# 6. Screenshot Realtime

### 1. Dashboard Saat Pertama Dibuka
![Dashboard](static/img/dashboard.png)

### 2. Update Status & Bandwidth (Realtime)
![Update Tabel](static/img/table_update.png)

### 3. Grafik Bandwidth Bergerak Real-Time
![Grafik](static/img/chart_update.png)

---

# 7. Penjelasan Arsitektur Aplikasi

Aplikasi menggunakan arsitektur **Client–Server dengan kombinasi REST API dan WebSocket**.

### **🔹 Frontend:**
- HTML (Jinja2 Flask Template)
- TailwindCSS (UI)
- Chart.js (grafik realtime)
- Socket.IO Client (menerima data realtime)

### **🔹 Backend (Flask + SocketIO):**
- Mengirim data device secara realtime setiap 2 detik
- Menyediakan endpoint REST API
- Background task berjalan sebagai “data generator”

### **🔹 Simulasi perangkat:**
Tiga perangkat disimulasikan dalam file `devices.py`:
- status online/offline
- bandwidth random  
- penyimpanan data history

---

# 8. Diagram Arsitektur

```
                ┌────────────────────┐
                │     Browser UI     │
                │   (Client Side)    │
                │                    │
                │ HTML + CSS + JS    │
                │ Chart.js + SocketIO│
                └──────────┬─────────┘
                           │
                 WebSocket │  REST API
                           │
                ┌──────────▼─────────┐
                │     Flask Server    │
                │   (app.py)          │
                │  - SocketIO Event   │
                │  - API Endpoint     │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │    devices.py       │
                │  Simulasi perangkat │
                │  - Status           │
                │  - Bandwidth        │
                └────────────────────┘
```

---

# 9. Kesimpulan

Kriteria tugas:

✔ 3 perangkat jaringan  
✔ Data realtime (WebSocket)  
✔ REST API  
✔ UI dashboard modern  
✔ Arsitektur jelas  
✔ Source code + screenshot + dokumentasi lengkap  

---

# 10. Identitas

Nama: Rifaldi Ahmad Rehan
NIM: 241091900397
Kelas: 03SKMM003

---




