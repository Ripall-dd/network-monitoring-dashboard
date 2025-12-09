import platform
import subprocess
import psutil
import random
from datetime import datetime

# Device list
devices = [
    {"name": "Router WiFi", "ip": "192.168.100.1", "status": "unknown", "bandwidth": 0, "mode": "sim"},
    {"name": "HP Android", "ip": "192.168.100.32", "status": "unknown", "bandwidth": 0, "mode": "sim"},
    {"name": "Laptop Saya", "ip": "192.168.100.33", "status": "unknown", "bandwidth": 0, "mode": "real"},
]

history = []

# For real bandwidth measurement
last_sent = psutil.net_io_counters().bytes_sent
last_recv = psutil.net_io_counters().bytes_recv

def ping(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    cmd = ["ping", param, "1", ip]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except:
        return False


def get_real_bandwidth():
    global last_sent, last_recv

    counters = psutil.net_io_counters()
    sent_now = counters.bytes_sent
    recv_now = counters.bytes_recv

    upload_mbps = ((sent_now - last_sent) * 8) / 1e6
    download_mbps = ((recv_now - last_recv) * 8) / 1e6

    last_sent = sent_now
    last_recv = recv_now

    return round(download_mbps, 2)  # atau upload_mbps


def update_devices():
    for d in devices:
        alive = ping(d["ip"])
        d["status"] = "online" if alive else "offline"

        # BANDWIDTH MODE
        if d["mode"] == "real":
            # Laptop bandwidth asli
            d["bandwidth"] = get_real_bandwidth() if alive else 0

        else:
            # Simulasi untuk HP & Router
            d["bandwidth"] = random.randint(5, 50) if alive else 0

    history.append({
        "time": datetime.now().isoformat(),
        "data": devices.copy()
    })

    if len(history) > 100:
        history.pop(0)

    return devices
