# 🔍 Threat Log Analyzer

**Threat Log Analyzer** is an **enterprise-grade log analysis tool** designed for **SOC teams** and **security professionals**. It scans system logs for **MITRE ATT&CK-aligned threats** like unauthorized access, failed login attempts, and malware indicators.

---

## 🚀 Features
- ✅ **Enterprise security patterns** with MITRE ATT&CK techniques  
- ✅ **Regex-based log analysis** for intrusion detection  
- ✅ **Automated JSON threat reports** for easy integration  
- ✅ **Error handling** for missing or inaccessible log files  
- ✅ **Optimized for SOC teams & cybersecurity enthusiasts**  

---

## 📂 Project Structure

Threat-Log-Analyzer/ │── sample_logs.txt # Sample log file │── threat_analyzer.py # Python script │── threats_found.json # Auto-generated threat report │── README.md # Project documentation


---

## 🛠 Installation & Usage

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yuvaraj-yeshwanth/threat-log-analyzer.git
cd threat-log-analyzer

2️⃣ Install Python (If Not Installed)

Ensure Python 3 is installed:

sudo apt update && sudo apt install python3

3️⃣ Run the Threat Analyzer

python3 threat_analyzer.py sample_logs.txt

📝 How It Works

    Reads log files and searches for threat indicators.

    Uses regex patterns (MITRE ATT&CK-aligned) to detect threats.

    Displays threats in the terminal.

    Generates a JSON report (threats_found.json) with detected threats.

🔍 Example Log File (sample_logs.txt)

2025-03-27 12:10:01 - User login successful: admin
2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22
2025-03-27 12:30:45 - Possible SQL injection attempt detected
2025-03-27 12:35:50 - MALWARE detected in system process

📌 Expected Output:

🔍 Detected 5 potential threats:
1. Failed login attempt from IP 192.168.1.10
2. Unauthorized access detected in /var/log/auth.log
3. ERROR: Connection timeout on port 22
4. Possible SQL injection attempt detected
5. MALWARE detected in system process

✅ Report generated: threats_found.json

🛡 Threat Detection Patterns

This tool detects the following keywords using regular expressions:

    🔹 failed → Failed login attempts

    🔹 unauthorized → Unauthorized access

    🔹 error → System errors

    🔹 intrusion → Intrusion attempts

    🔹 malware → Malware detection

    🔹 attack → Attack signatures

    🔹 breach → Data breaches

    🔹 exploit → Exploit attempts

    🔹 injection → SQL or command injections

📊 JSON Threat Report Format

{
  "meta": {
    "system": "Threat Log Analyzer",
    "version": "1.1",
    "detected_threats": 5
  },
  "findings": [
    "Failed login attempt from IP 192.168.1.10",
    "Unauthorized access detected in /var/log/auth.log",
    "ERROR: Connection timeout on port 22",
    "Possible SQL injection attempt detected",
    "MALWARE detected in system process"
  ]
}

🚀 Future Improvements

    🔹 Real-time log monitoring

    🔹 SIEM integration (Splunk, ELK, etc.)

    🔹 Threat severity scoring

    🔹 Email alerts & notifications

📢 Connect With Me

👤 Yuvaraj M
🔗 LinkedIn: My LinkedIn Profile

If this project helps you, give it a ⭐ on GitHub! 🚀
