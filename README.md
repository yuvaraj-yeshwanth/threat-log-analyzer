# Threat Log Analyzer

Hi! I'm Yuvaraj, a cybersecurity enthusiast. This tool helps detect security threats in log files using Python. 
Perfect for SOC analysts or anyone learning log analysis!

## Features
- Detects failed logins, unauthorized access, errors
- Simple regex-based pattern matching
- Saves threats to JSON file
- Beginner-friendly

## Files
- threat_log_analyzer.py : Main Python script
- security_logs.txt      : Sample log file
- threats_found.json     : Output example

## How to Run

1. Clone the repo:
git clone https://github.com/yuvaraj-yeshwanth/threat-log-analyzer.git
cd threat-log-analyzer

2. Run the script:
python3 threat_log_analyzer.py security_logs.txt

3. See output:
Potential threats will appear in terminal and save to threats_found.json

## Sample Output

2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10  
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log  
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22  

## Why I Made This
- Practice log analysis skills
- Learn Python for cybersecurity
- Create tools for SOC workflows

## Connect
LinkedIn: https://www.linkedin.com/in/yuvaraj-m-b718151b9  
GitHub: https://github.com/yuvaraj-yeshwanth

Feel free to contribute or suggest improvements!
