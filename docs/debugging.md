# 🐞 Debugging Report - Computer Fingerprint Collector

This document records the debugging process used during development of the Computer Fingerprint Collector script.  
All debugging was performed using **Visual Studio Code** with the Python extension.

---

## 1. Breakpoint at Internet Speed Test

A breakpoint was set inside the `test_internet_speed()` function to verify:

- Speedtest module behaviour  
- Exception handling  
- Return values when offline  
- Object structure of the Speedtest instance  

**Screenshot:**  
![SpeedTest](https://raw.githubusercontent.com/AlAbbas-cloud/computer-fingerprint-collector/refs/heads/main/docs/images/debug_breakpoint.png)

---

## 2. Active Debugging Session (Call Stack + Watch Expressions)

During execution, the debugger displayed:

- Full call stack  
- Local variables  
- Watch expressions for system info fields  
- Breakpoints across multiple functions  

This confirmed correct function flow and validated intermediate values.

**Screenshot:**  
![Call-Stack](https://raw.githubusercontent.com/AlAbbas-cloud/computer-fingerprint-collector/refs/heads/main/docs/images/debug_callstack.png)

---

## 3. Debugging System Information Functions

The following functions were individually tested:

- `get_mac_address()`  
- `get_ip_address()`  
- `get_system_info()`  
- `get_network_info()`  

Debugging verified:

- Correct MAC formatting  
- OS detection  
- Processor model extraction  
- Error handling for missing interfaces  

**Screenshot:**  
![SysInfo](https://raw.githubusercontent.com/AlAbbas-cloud/computer-fingerprint-collector/refs/heads/main/docs/images/debug_systeminfo.png)

---

## 4. Debugger Paused at Internet Speed Test

The debugger was paused inside the speed test function to inspect:

- Speedtest object in memory  
- Network exceptions  
- Fallback behaviour when offline  
- Impact of `justMyCode` setting  

**Screenshot:**  
![Speed-test](https://raw.githubusercontent.com/AlAbbas-cloud/computer-fingerprint-collector/refs/heads/main/docs/images/debug_justmycode.png)

---

## 5. Live Debugging Session (Evaluated Values)

A live session confirmed:

- Internet speed values were correctly parsed  
- System info dictionary was populated correctly  
- Sanitisation and validation functions behaved as expected  

**Screenshot:**  
![JustMyCode](https://raw.githubusercontent.com/AlAbbas-cloud/computer-fingerprint-collector/refs/heads/main/docs/images/debug_speedtest.png)

---

## Summary

Debugging confirmed:

- All functions behave correctly  
- Error handling works across Windows and Linux  
- CSV writing logic is stable  
- Network functions fail gracefully when offline  
- The script is production‑ready for Midtown IT

