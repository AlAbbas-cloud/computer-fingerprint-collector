## How to Run the Computer Fingerprint Collector

This script collects system and network information from Windows and Linux computers and saves the results into a CSV file.

---

### **1. Requirements**

- Python 3.x installed  
- No third‑party libraries required (standard library only)  
- Permission to run Python scripts on the system  

---

### **2. Download or Clone the Repository**

```bash
git clone https://github.com/AlAbbas-cloud/computer-fingerprint-collector.git
cd computer-fingerprint-collector/src
```
---

### **3. Run the Script**
**Windows**
```bash
python computer_fingerprint_collector.py
```
**Linux / macOS**
```bash
python3 computer_fingerprint_collector.py
```

---

### **4. Output Location**
After running, a file named:
```code
computer_fingerprints.csv
```
will appear in the same folder as the script.

Each run appends a new entry containing:

- Computer name
- IP address
- MAC address
- Processor model
- Operating system
- System time
- Internet speed
- Active ports
- Unique ID
- Timestamp

---

## Script Flow Diagram
+------------------------------------------------------+
|                START PROGRAM                         |
+------------------------------------------------------+
                      |
                      v
        +-------------------------------+
        | Collect System Information    |
        | - Computer name               |
        | - OS & version                |
        | - Processor model             |
        | - System time                 |
        +-------------------------------+
                      |
                      v
        +-------------------------------+
        | Collect Network Information   |
        | - IP address                  |
        | - MAC address                 |
        | - Active ports                |
        +-------------------------------+
                      |
                      v
        +-------------------------------+
        | Test Internet Speed           |
        +-------------------------------+
                      |
                      v
        +-------------------------------+
        | Get Unique Computer ID        |
        +-------------------------------+
                      |
                      v
        +-------------------------------+
        | Validate & Sanitise Data      |
        +-------------------------------+
                      |
                      v
        +-------------------------------+
        | Does CSV File Exist?          |
        +-------------------------------+
             |                     |
             | Yes                 | No
             v                     v
 +---------------------+   +------------------------+
 | Append to CSV File  |   | Create CSV + Write Row |
 +---------------------+   +------------------------+
             \             /
              \           /
               \         /
                v       v
        +-------------------------------+
        | Print Success Message         |
        +-------------------------------+
                      |
                      v
              +----------------+
              |     END        |
              +----------------+
