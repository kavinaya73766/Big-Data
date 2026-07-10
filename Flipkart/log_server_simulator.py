"""
log_server_simulator.py
------------------------
Pretends to be 3 "high-velocity" Flipkart regional servers
(Flipkart-Chennai, Flipkart-Bangalore, Flipkart-Mumbai).

Each one is a tiny TCP server that, the moment a client
(our harvester daemon) connects, starts firing log lines
continuously, forever, at random intervals.

Run this FIRST, in its own terminal, and leave it running.
"""

import socket
import threading
import random
import time
from datetime import datetime

# One (name, port) per simulated Flipkart regional server
REGIONS = [
    ("flipkart-chennai", 9001),
    ("flipkart-bangalore", 9002),
    ("flipkart-mumbai", 9003),
]

LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]

# Sample message templates per level
MESSAGE_TEMPLATES = {
    "INFO": [
        "Order#{oid} placed successfully",
        "Order#{oid} shipped from warehouse",
        "Order#{oid} delivered to customer",
        "Seller accepted Order#{oid}",
    ],

    "WARNING": [
        "Order#{oid} delivery delayed by 1 day",
        "Warehouse stock running low for Product#{oid}",
        "High order volume detected for Product#{oid}",
    ],

    "ERROR": [
        "Payment failed for Order#{oid}",
        "Order#{oid} cancelled due to out of stock",
        "Delivery tracking unavailable for Order#{oid}",
    ],

    "DEBUG": [
        "Cache miss while fetching Product#{oid}",
        "Retrying database update for Order#{oid}",
    ],
}


def build_log_line(region_name):
    """Builds one well-formed log line."""
    
    level = random.choice(LEVELS)
    oid = random.randint(1000, 9999)

    message = random.choice(
        MESSAGE_TEMPLATES[level]
    ).format(oid=oid)

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return (
        f"{timestamp} | "
        f"{level} | "
        f"{region_name} | "
        f"{message}\n"
    )


def handle_client(conn, region_name):
    """Continuously sends logs to the harvester."""

    print(
        f"[{region_name}] "
        f"harvester connected, streaming logs..."
    )

    try:
        while True:
            line = build_log_line(region_name)

            conn.sendall(
                line.encode("utf-8")
            )

            # Simulates burst traffic
            time.sleep(
                random.uniform(0.05, 0.4)
            )

            # Occasionally send corrupted data
            if random.random() < 0.05:
                conn.sendall(
                    b"INVALID_LOG_LINE\n"
                )

    except (
        BrokenPipeError,
        ConnectionResetError
    ):
        print(
            f"[{region_name}] "
            f"harvester disconnected."
        )

    finally:
        conn.close()


def run_region_server(region_name, port):
    server_sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1,
    )

    server_sock.bind(
        ("127.0.0.1", port)
    )

    server_sock.listen(1)

    print(
        f"[{region_name}] "
        f"listening on port {port}..."
    )

    while True:
        conn, addr = server_sock.accept()

        client_thread = threading.Thread(
            target=handle_client,
            args=(conn, region_name),
            daemon=True,
        )

        client_thread.start()


if __name__ == "__main__":
    threads = []

    for name, port in REGIONS:
        t = threading.Thread(
            target=run_region_server,
            args=(name, port),
            daemon=True,
        )

        t.start()
        threads.append(t)

    print(
        "\nAll Flipkart regional servers are up."
    )

    print(
        "Press Ctrl+C to stop.\n"
    )

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print(
            "\nShutting down simulator."
        )