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

## Script Flow Diagram (Mermaid)

```mermaid
flowchart TD

    A([Start Program]) --> B[Collect System Information<br/>• Computer name<br/>• OS & version<br/>• Processor model<br/>• System time]

    B --> C[Collect Network Information<br/>• IP address<br/>• MAC address<br/>• Active ports]

    C --> D[Test Internet Speed]

    D --> E[Get Unique Computer ID]

    E --> F[Validate & Sanitise Data]

    F --> G{Does CSV File Exist?}

    G -->|Yes| H[Append to CSV File]
    G -->|No| I[Create CSV File<br/>+ Write First Row]

    H --> J[Print Success Message]
    I --> J[Print Success Message]

    J --> K([End])

