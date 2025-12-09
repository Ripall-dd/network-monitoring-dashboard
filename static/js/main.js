const socket = io();

// CHART INITIALIZATION
let labels = [];
const ctx = document.getElementById("bandChart");

const bandChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: labels,
        datasets: [
            { label: "Router A", data: [], borderColor: "rgba(128, 0, 255, 1)" },
            { label: "Switch B", data: [], borderColor: "rgba(255, 0, 128, 1)" },
            { label: "Server C", data: [], borderColor: "rgba(255, 128, 128, 1)" }
        ]
    },
    options: { responsive: true }
});

// WEBSOCKET UPDATE
socket.on("update", (devices) => {

    // Update table
    const table = document.getElementById("deviceTable");
    table.innerHTML = `
        <tr class='border-b border-gray-700 text-gray-300'>
            <th class="py-2">Nama</th>
            <th>IP Address</th>
            <th>Status</th>
            <th>Bandwidth</th>
        </tr>
    `;

    let timestamp = new Date().toLocaleTimeString();
    labels.push(timestamp);

    devices.forEach((d, index) => {

        let color = d.status === "online" ? "bg-green-600" : "bg-red-600";

        table.innerHTML += `
            <tr class="border-b border-gray-700">
                <td class="py-2">${d.name}</td>
                <td>${d.ip}</td>
                <td><span class="px-2 py-1 rounded-full text-sm ${color}">${d.status}</span></td>
                <td>${d.bandwidth} Mbps</td>
            </tr>
        `;

        // Update chart
        bandChart.data.datasets[index].data.push(d.bandwidth);
    });

    if (labels.length > 15) {
        labels.shift();
        bandChart.data.datasets.forEach(ds => ds.data.shift());
    }

    bandChart.update();

    // Log
    document.getElementById("log").innerHTML =
        `<div>[${timestamp}] Data diperbarui</div>` +
        document.getElementById("log").innerHTML;
});

socket.on("log_update", (msg) => {
    const box = document.getElementById("log");

    msg.logs.forEach(text => {
        const line = document.createElement("div");

        line.textContent = `${msg.timestamp} ${text}`;

        // Warna log
        if (text.includes("────"))       line.className = "text-yellow-400";
        else if (text.startsWith("EVENT")) line.className = "text-red-400";
        else                                line.className = "text-blue-300";

        box.prepend(line);
    });
});
