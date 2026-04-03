# 🖥️ Computer Fingerprint Collector  
### Automated Processes Algorithmic & Scripting Solution Report  
**Student:** Ali Abbas  
**Client:** Midtown IT  
**Units:** ICTPRG434 / ICTPRG435  
**Date:** 13 May 2025  
**Version:** 1.1  

---

# 1. Project Overview

Midtown IT requires an automated solution to collect system and network information from all computers across the organisation. The collected data must be stored in a Microsoft Excel–compatible CSV file and updated whenever the script is run.

The solution must:

- Use **Python 3.x**  
- Use **standard library only** (no third‑party packages)  
- Follow **Midtown IT Python Coding Style Guidelines**  
- Be secure, defensive, and cross‑platform (Windows + Linux)  
- Be fully documented, tested, and verified  

---

# 2. Application Requirements

## 2.1 Purpose of the Application
The program collects key system and network information from each computer at Midtown IT and stores it in a CSV file for auditing and asset management.

## 2.2 Process to Be Automated
- Run the script on each computer (Windows or Linux)  
- Collect system + network details  
- Validate and sanitise data  
- Append or create a CSV file  
- Store results on USB or shared folder  

## 2.3 Expected Outcomes
The script must collect:

- Computer Name  
- IP Address  
- MAC Address  
- Processor Model  
- Operating System  
- System Time  
- Internet Speed  
- Active Ports  
- Timestamp  
- Unique Computer ID (if available)

## 2.4 Client Expectations

### Functionality
- Works on Windows & Linux  
- Collects only required data  
- Handles errors safely  
- Easy to run  

### Security
- Validates and sanitises all data  
- Avoids sensitive information  
- Defensive coding style  
- No third‑party libraries  

## 2.5 Operating Environment

### Hardware
- Desktop & laptop computers  
- Ethernet/Wi‑Fi network cards  

### Software
- Windows 10/11  
- Linux (Ubuntu, Fedora, etc.)  
- Python 3.x  

### Services
- DHCP, DNS  
- Internet access  
- USB or shared folder for storage  

---

# 3. Requirements Confirmation

A meeting was held with the IT Manager (Hadi) to confirm requirements.  
Feedback included: 

- All listed data points are required  
- Must include timestamp  
- Include unique computer ID if available  
- Use only Python standard library  
- Emphasise error handling and validation  

**Updated requirements have been incorporated.**

---

# 4. Solution Options & Final Decision

## 4.1 Potential Solutions

### **Solution 1 — Local Script + CSV Output**
- Run manually on each machine  
- Saves CSV locally or to USB  

### **Solution 2 — Centralised Server Reporting**
- Each machine sends data to a central server  

### **Solution 3 — Scheduled Script + Shared Folder Output**
- Script runs via Task Scheduler / cron  
- Saves CSV to shared folder  

## 4.2 Final Decision
**Solution 3 selected** because it:  
- Automates collection  
- Requires no new infrastructure  
- Works cross‑platform  
- Uses only standard libraries  
- Is secure and maintainable  

---

# 5. Algorithmic Solution

## 5.1 Pseudocode

```code
BEGIN

SET current_time = get current system time
SET computer_name = get computer name
SET ip_address = get IP address
SET mac_address = get MAC address
SET processor_model = get processor model
SET operating_system = get OS name and version
SET internet_speed = test internet download speed
SET active_ports = get list of open ports
SET unique_id = get system UUID or serial number

VALIDATE all collected data
SANITISE data to remove unwanted characters

IF CSV file exists THEN
APPEND new row with collected data
ELSE
CREATE new CSV file with headers
ADD collected data as first row
ENDIF

END
```
