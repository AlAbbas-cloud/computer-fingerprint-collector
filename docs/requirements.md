# Application Requirements - Computer Fingerprint Collector

This document outlines the functional, technical, and security requirements for the Computer Fingerprint Collector project, based on the Midtown IT scenario.

---

# 1. Purpose

To collect and store key system and network information from all computers used at Midtown IT.  
The script outputs a CSV file compatible with Microsoft Excel.

---

# 2. Process to Be Automated

- Run the script on each computer (Windows or Linux)  
- Collect system + network details  
- Validate and sanitise data  
- Append or create a CSV file  
- Store results on USB or shared folder  

---

# 3. Data to Be Collected

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

---

# 4. Client Expectations

## 4.1 Functionality
- Works on Windows and Linux  
- Collects only required data  
- Handles errors safely  
- Easy to run on any machine  

## 4.2 Security
- Validate and sanitise all data  
- Avoid sensitive information  
- Use defensive coding practices  
- Use only Python standard library  

---

# 5. Operating Environment

## Hardware
- Desktop and laptop computers  
- Ethernet/Wi‑Fi network cards  

## Software
- Windows 10/11  
- Linux (Ubuntu, Fedora, etc.)  
- Python 3.x  
- No third‑party libraries  

## Services
- DHCP, DNS  
- Internet access  
- USB or shared folder for storage  

---

# 6. Constraints

- Must follow Midtown IT Python Coding Style Guidelines  
- Must use standard library only  
- Must be cross‑platform  
- Must be secure and defensively coded  

---

# 7. Approved Solution Summary

**Solution 3 — Scheduled Script + Shared Folder Output**

- Automates data collection  
- No new infrastructure required  
- Works cross‑platform  
- Secure and maintainable  
- Uses only built‑in Python libraries  

---

# 8. Acceptance Criteria

The solution is considered complete when:

- Script runs successfully on Windows and Linux  
- All required data fields are collected  
- CSV file is created or updated correctly  
- Data is validated and sanitised  
- Documentation is complete  
- Testing is successful  

