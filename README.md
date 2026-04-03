/ |  _ __  _ __   ___  | | _ __ ___  | | ___  _ __
| |   / _ \| ' \| ' \ / _ \/ | | '/ _ \/ | / _ \| '|
| || () | | | | | | |  /\ \ || | |  / (| || () | |
\____\/|| ||| ||\||/\||  \|\|\\_/||

# Computer Fingerprint Collector  
### Cross‑Platform System & Network Information Automation Script

This project automates the collection of system and network information from Windows and Linux machines.  
It was developed as part of the **Midtown IT Automation & Scripting Assessment** and is designed using **defensive coding**, **cross‑platform compatibility**, and **zero third‑party dependencies**.

---

## 📑 Table of Contents

- [Project Overview](#️-computer-fingerprint-collector)
- [Features](#-features)
- [Repository Structure](#-repository-structure)
- [How to Run](#️-how-to-run-the-script)
- [Script Flow Diagram](#-script-flow-diagram-mermaid)
- [Sample Output](#-sample-output)
- [Debugging Documentation](#-debugging-documentation)
- [Documentation](#-documentation)
- [Status](#️-status)
- [Author](#-author)

## Features

- Collects detailed **system information**  
- Collects **network information** (IP, MAC, active ports)  
- Performs a lightweight **internet connectivity test**  
- Generates a **unique system identifier**  
- Validates and sanitises all collected data  
- Outputs to a **CSV file compatible with Excel**  
- Works on **Windows 10/11** and **Linux distributions**  
- Uses **Python standard library only**  
- Designed with **modular, maintainable functions**  
- Includes **debugging documentation** and **sample outputs**

---

## Repository Structure

computer-fingerprint-collector/
│
├── src/
│   └── computer_fingerprint_collector.py
│
├── docs/
│   ├── pseudocode.md
│   ├── requirements.md
│   ├── debugging.md
│   └── images/
│       ├── debug_speedtest.png
│       ├── debug_callstack.png
│       ├── debug_systeminfo.png
│       ├── debug_justmycode.png
│       └── debug_live.png
│
├── samples/
│   └── sample_output.csv
│
└── README.md

