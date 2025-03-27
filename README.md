# 🔍 Threat Log Analyzer

**Threat Log Analyzer** is a simple Python tool that scans system log files for security threats. It detects **failed login attempts, unauthorized access, and errors** using regex pattern matching.  

This project is ideal for **SOC analysts**, **cybersecurity learners**, and anyone interested in **log analysis**.  

---

## 🛠 Features
- ✅ Scans log files for **failed logins, unauthorized access, and system errors**  
- ✅ Uses **Python regex** for threat detection  
- ✅ Saves detected threats to a JSON file  
- ✅ Beginner-friendly and easy to use  
- ✅ Can be extended for **SIEM integration**  

---

## 📂 Project Structure

Threat-Log-Analyzer/ │── security_logs.txt # Sample log file │── threat_log_analyzer.py # Python script │── threats_found.json # Detected threats (auto-generated) │── README.md # Project documentation


---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yuvaraj-yeshwanth/threat-log-analyzer.git
cd threat-log-analyzer

2️⃣ Install Python (If Not Installed)

Ensure Python is installed. If not, install it:

sudo apt update && sudo apt install python3

3️⃣ Run the Python Script

python3 threat_log_analyzer.py security_logs.txt

📝 How It Works

    Reads the log file (security_logs.txt).

    Searches for keywords like failed, unauthorized, and error.

    Displays potential threats from the logs.

    Saves the detected threats to threats_found.json.

📌 Example Log File (security_logs.txt)

2025-03-27 12:10:01 - User login successful: admin
2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22

📌 Expected Output:

🚨 Potential Threats Found:
2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22

✅ Threats saved to 'threats_found.json'

🎯 Why I Built This

I created this project to practice log analysis and showcase my cybersecurity skills. If you're new to SOC analysis, this project is a great way to start analyzing logs like a pro! 🚀
🚀 Future Improvements

    🔹 Live log monitoring

    🔹 Log visualization with graphs

    🔹 Automated alerts for critical threats

📢 Connect With Me

🔗 LinkedIn: My LinkedIn Profile

If you find this useful, give it a ⭐ on GitHub! 🚀


---

### ✅ **Next Steps:**
1. **Save this file** as `README.md`.  
2. **Commit & push** it to your GitHub repository:
   ```sh
   git add README.md
   git commit -m "Added README file"
   git push origin main
