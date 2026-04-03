"""
Computer Fingerprint Collector
Author: Ali Abbas
Purpose:
    Collect system and network information from Windows/Linux computers
    and store the results in a CSV file using a defensive coding style.
"""

import os
import csv
import platform
import socket
import uuid
import subprocess
from datetime import datetime


# ============================================================
#  SYSTEM INFORMATION
# ============================================================

def get_system_info():
    """Return system-level information such as hostname, OS, CPU, and time."""
    return {
        "computer_name": platform.node(),
        "processor_model": platform.processor(),
        "operating_system": f"{platform.system()} {platform.release()}",
        "system_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# ============================================================
#  NETWORK INFORMATION
# ============================================================

def get_ip_address():
    """Return the primary IP address."""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "Unknown"


def get_mac_address():
    """Return MAC address using UUID."""
    try:
        mac = uuid.getnode()
        return ':'.join([f"{(mac >> ele) & 0xff:02x}" for ele in range(40, -1, -8)])
    except Exception:
        return "Unknown"


def get_active_ports():
    """Return a list of active ports using netstat."""
    try:
        result = subprocess.check_output(["netstat", "-an"], text=True)
        ports = []
        for line in result.splitlines():
            if "LISTEN" in line or "ESTABLISHED" in line:
                parts = line.split()
                if ":" in parts[1]:
                    port = parts[1].split(":")[-1]
                    if port.isdigit():
                        ports.append(port)
        return ";".join(sorted(set(ports)))
    except Exception:
        return "Unknown"


def get_network_info():
    """Return all network-related information."""
    return {
        "ip_address": get_ip_address(),
        "mac_address": get_mac_address(),
        "active_ports": get_active_ports()
    }


# ============================================================
#  INTERNET SPEED
# ============================================================

def test_internet_speed():
    """Return simple online/offline status using ping."""
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"], text=True)
        return "Online"
    except Exception:
        return "Offline"


# ============================================================
#  UNIQUE IDENTIFIER
# ============================================================

def get_unique_id():
    """Return a unique system identifier."""
    try:
        return str(uuid.uuid4())
    except Exception:
        return "Unknown"


# ============================================================
#  VALIDATION & SANITISATION
# ============================================================

def validate_data(data: dict) -> bool:
    """Ensure no field is empty, None, or unsafe."""
    return all(value not in ("", None, "Unknown") for value in data.values())


def sanitise_data(data: dict) -> dict:
    """Remove commas and unsafe characters from all fields."""
    clean = {}
    for key, value in data.items():
        clean[key] = str(value).replace(",", ";").strip()
    return clean


# ============================================================
#  CSV HANDLING
# ============================================================

CSV_FILE = "computer_fingerprints.csv"

def csv_exists():
    return os.path.isfile(CSV_FILE)


def write_new_csv(data: dict):
    """Create a new CSV file with headers and first row."""
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)


def append_to_csv(data: dict):
    """Append a new row to an existing CSV file."""
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)


# ============================================================
#  MAIN WORKFLOW
# ============================================================

def main():
    """Main program workflow."""
    system_info = get_system_info()
    network_info = get_network_info()
    internet_speed = {"internet_speed": test_internet_speed()}
    unique_id = {"unique_id": get_unique_id()}

    # Merge all data
    data = {**system_info, **network_info, **internet_speed, **unique_id}

    # Validate & sanitise
    if not validate_data(data):
        print("Error: Missing or invalid data. Aborting.")
        return

    data = sanitise_data(data)

    # Write to CSV
    if csv_exists():
        append_to_csv(data)
    else:
        write_new_csv(data)

    print("Computer fingerprint collected successfully.")


if __name__ == "__main__":
    main()
