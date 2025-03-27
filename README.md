# Threat Log Analyzer 🔍

Hey there! I'm **Yuvaraj**, a cybersecurity enthusiast passionate about log analysis and threat detection. This tool helps identify security events in system logs - perfect for SOC analysts and beginners!

---

## 🛠 Features
- ✅ Detect failed login attempts
- ✅ Identify unauthorized access
- ✅ Catch system errors
- ✅ Export results to JSON
- ✅ Beginner-friendly Python implementation

---

## 📂 Project Structure

Threat-Log-Analyzer/
├── security_logs.txt # Sample log file
├── threat_log_analyzer.py # Main analysis script
└── README.md # Documentation


---

## 🚀 Quick Start

### 1. Clone & Run
```sh
git clone https://github.com/yuvaraj-yeshwanth/threat-log-analyzer.git
cd threat-log-analyzer
python3 threat_log_analyzer.py

2. Sample Output

🚨 Potential Threats Found:
2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22
2025-03-27 12:35:50 - Malware detected in file /tmp/suspicious.exe
2025-03-27 12:40:10 - Intrusion attempt detected from IP 10.0.0.5

✅ Threats saved to 'threats_found.json'

🛠 Custom Usage

# Analyze custom log files
python3 threat_log_analyzer.py path/to/your/logfile.log

🎯 Why I Built This

    Practice log analysis fundamentals

    Demonstrate threat detection capabilities

    Create beginner-friendly security tool

    Showcase Python skills for SOC roles

🔮 Future Plans

    Real-time log monitoring

    Threat severity classification

    Email/SMS alerts

    Dashboard integration

🤝 Connect & Contribute

LinkedIn

Star ⭐ the repo if you find this useful!
Open to collaborations and suggestions!
