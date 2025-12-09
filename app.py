import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import device
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Menyimpan status lama untuk deteksi perubahan
old_status = {}  


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/history")
def history():
    return jsonify(device.history)


def build_log(devices):
    """
    Log akan SELALU cocok dengan tabel,
    karena log dibangun menggunakan data devices
    yang BARU SAJA dipakai update UI.
    """
    global old_status
    logs = []

    logs.append("──────── UPDATE SESSION ────────")

    for d in devices:
        name = d["name"]
        current = d["status"]
        prev = old_status.get(name)

        # Log perubahan status
        if prev is not None and prev != current:
            logs.append(f"EVENT: {name} berubah menjadi {current.upper()}")

        # Log info status terbaru (selalu sesuai table)
        logs.append(
            f"INFO: {name} → {current.upper()} | {d['bandwidth']} Mbps"
        )

    # update status lama SETELAH log selesai
    old_status = {d["name"]: d["status"] for d in devices}

    return logs


def background_update():
    while True:
        # update_devices menghasilkan data FINAL untuk 1 cycle
        devices_now = device.update_devices()

        # Kirim ke tabel & grafik
        socketio.emit("update", devices_now)

        # Buat log berdasarkan device NOW (tidak bisa tertukar)
        logs = build_log(devices_now)

        # Kirim ke UI log panel
        socketio.emit("log_update", {
            "timestamp": time.strftime("[%H:%M:%S]"),
            "logs": logs
        })

        socketio.sleep(2)


@socketio.on("connect")
def connected():
    print("Client connected")


if __name__ == "__main__":
    socketio.start_background_task(background_update)
    socketio.run(app, host="0.0.0.0", port=5000, debug=True, allow_unsafe_werkzeug=True)
