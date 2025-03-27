# Threat Log Analyzer

## 🚀 Overview
The **Threat Log Analyzer** is a Python-based tool that scans log files to detect potential security threats like:
- ✅ **Failed login attempts**
- ✅ **Unauthorized access**
- ✅ **Error logs**

This project is useful for **SOC analysts** and **Threat Analysts** to analyze logs and identify suspicious activities.

---

## 🛠️ Features
- 🔍 **Log file scanning** for security threats
- 🎯 Detects **failed logins, unauthorized access, and errors**
- ⚡ Simple and easy-to-use Python script
- 🔄 Can be extended for **SIEM integration**

---

## 📂 Project Structure
```
Threat-Log-Analyzer/
│── security_logs.txt        # Sample log file
│── threat_log_analyzer.py   # Python script
│── README.md                # Project documentation
```

---

## 📌 How to Use

### 1️⃣ **Prepare a Log File**
Create a file named **`security_logs.txt`** and add logs like this:
```txt
2025-03-27 12:10:01 - User login successful: admin
2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22
```

### 2️⃣ **Run the Python Script**
1. Ensure you have **Python installed**.
2. Save the script below as `threat_log_analyzer.py`.
3. Run the script:
   ```sh
   python threat_log_analyzer.py
   ```

### 3️⃣ **Check the Output**
```
Potential Threats Found:
2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22
```

---

## 📝 Code Explanation
```python
import re

def parse_logs(file_path):
    with open(file_path, 'r') as f:
        logs = f.readlines()
    
    threats = []
    pattern = re.compile(r'failed|unauthorized|error', re.IGNORECASE)
    
    for log in logs:
        if pattern.search(log):
            threats.append(log.strip())
    
    return threats

if __name__ == "__main__":
    file_path = "security_logs.txt"
    threats_found = parse_logs(file_path)
    
    print("Potential Threats Found:")
    for threat in threats_found:
        print(threat)
```
### 🔹 How It Works
- **Reads log files** line by line.
- **Searches for security-related keywords** (`failed`, `unauthorized`, `error`).
- **Filters out threats** and displays them.

---

## 📤 Uploading to GitHub
1. **Create a GitHub repository** (e.g., `Threat-Log-Analyzer`).
2. Click **"Add file" → "Upload files"**.
3. **Upload** the following files:
   ✅ `threat_log_analyzer.py`
   ✅ `security_logs.txt`
   ✅ `README.md`
4. Click **"Commit changes"**. 🎉

---

## 🎯 Why This Project is Useful
✅ **Real-world SOC use case** (log analysis for threats).  
✅ **Hands-on security experience** (regex & log parsing).  
✅ **Easy to expand** (can be integrated with SIEM tools).  

---

## 🚀 Future Improvements
- 🔹 Add **live log monitoring**.
- 🔹 Implement **log visualization**.
- 🔹 Automate **alerts for high-risk threats**.

---

## 👨‍💻 Author
**Yuvaraj** - Cybersecurity Enthusiast & Threat Analyst

🔗 **GitHub:** [My GitHub Profile](https://github.com/yuvaraj-yeshwanth)  
🔗 **LinkedIn:** [My LinkedIn Profile](https://www.linkedin.com/in/yuvaraj-m-b718151b9/)
