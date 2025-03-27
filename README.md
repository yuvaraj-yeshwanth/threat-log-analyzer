# Threat Log Analyzer

## 🔥 Introduction
Hey there! I'm **Yuvaraj**, and I created this **Threat Log Analyzer** to help analyze log files for security threats. If you're into **cybersecurity**, especially SOC analysis, this tool will help you detect failed login attempts, unauthorized access, and errors in system logs. 

This is a beginner-friendly project, and I made it easy for anyone to set up and use. If you're new to log analysis, this will be a great starting point!

---

## 🛠 Features
- ✅ Scans log files for **failed login attempts, unauthorized access, and errors**
- ✅ Uses **simple Python regex** for threat detection
- ✅ Can be extended for **SIEM integration**
- ✅ Helps understand **log analysis** in SOC roles

---

## 📂 Project Structure
```
Threat-Log-Analyzer/
│── security_logs.txt        # Sample log file
│── threat_log_analyzer.py   # Python script
│── README.md                # Project documentation
```

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yuvaraj-yeshwanth/threat-log-analyzer.git
cd threat-log-analyzer
```

### 2️⃣ Install Python (If Not Installed)
Make sure you have Python installed. If not, install it:
```sh
sudo apt update && sudo apt install python3
```

### 3️⃣ Run the Python Script
```sh
python3 threat_log_analyzer.py
```

---

## 📝 How It Works
1. **Reads the log file** (`security_logs.txt`).
2. **Searches for keywords** like `failed`, `unauthorized`, and `error`.
3. **Displays potential threats** from the logs.

Example log file (`security_logs.txt`):
```txt
2025-03-27 12:10:01 - User login successful: admin
2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22
```

Output:
```sh
Potential Threats Found:
2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22
```

---

## 🎯 Why I Built This
I wanted to create a simple tool to **practice log analysis** and **showcase my skills on GitHub**. If you're learning **SOC analysis**, this project is a great way to get hands-on experience.

---

## 🚀 Future Improvements
- 🔹 Add **live log monitoring**.
- 🔹 Implement **log visualization**.
- 🔹 Automate **alerts for high-risk threats**.

---

## 📢 Connect With Me

🔗 **LinkedIn:** [My LinkedIn Profile](https://www.linkedin.com/in/yuvaraj-m-b718151b9/)  

If you find this useful, **give it a ⭐ on GitHub!** 🚀
