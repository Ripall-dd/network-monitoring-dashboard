# 📡 Network Monitoring Dashboard (Real Device)

Tugas Mata Kuliah: **Komunikasi Data**  
Nama: **Rifaldi Ahmad Rehan**
NIM: **241091900397**

Aplikasi monitoring jaringan real-time menggunakan **Flask + Socket.IO** dengan data yang diambil dari **perangkat nyata**:

- **Router WiFi** → ICMP Ping  
- **HP Android** → ICMP Ping  
- **Laptop** → Bandwidth asli via psutil  

Dashboard menampilkan status perangkat, grafik bandwidth, dan log aktivitas yang diperbarui otomatis setiap **2 detik**.

---

## 🚀 Fitur Utama

- Monitoring real-time (WebSocket)
- Status online/offline perangkat real
- Bandwidth asli dari laptop
- Log aktivitas otomatis

---

# 2. Struktur Folder

```
network-monitoring-dashboard/
│
├── app.py
├── device.py
├── requirements.txt
├── Readme.md
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





