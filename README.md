# =================================================================
# 🔍 THREAT LOG ANALYZER - ENTERPRISE SECURITY TOOL
# =================================================================
# Author: Yuvaraj M
# LinkedIn: https://linkedin.com/in/yuvaraj-m-b718151b9
# Repo: https://github.com/yuvaraj-yeshwanth/threat-log-analyzer
# =================================================================

# Clone and setup
git clone https://github.com/yuvaraj-yeshwanth/threat-log-analyzer.git && cd threat-log-analyzer

# Create sample log file
cat <<EOF > sample_logs.txt
2025-03-27 12:10:01 - User login successful: admin
2025-03-27 12:15:20 - Failed login attempt from IP 192.168.1.10
2025-03-27 12:20:05 - Unauthorized access detected in /var/log/auth.log
2025-03-27 12:25:30 - ERROR: Connection timeout on port 22
2025-03-27 12:35:50 - MALWARE detected in system process
EOF

# Run analysis with output
echo -e "\n\033[1;34m🔍 ANALYZING LOGS...\033[0m"
python3 threat_log_analyzer.py sample_logs.txt

# Show results
echo -e "\n\033[1;32m📄 THREAT REPORT:\033[0m"
cat threats_found.json

# =================================================================
# EXPECTED OUTPUT:
# 🔍 Detected 4 potential threats:
# 1. Failed login attempt from IP 192.168.1.10
# 2. Unauthorized access detected in /var/log/auth.log 
# 3. ERROR: Connection timeout on port 22
# 4. MALWARE detected in system process
# ✅ Report generated: threats_found.json
# =================================================================

# =================================================================
# KEY FEATURES:
# - MITRE ATT&CK-aligned patterns
# - Automated JSON reporting
# - SOC-ready implementation
# - Error handling & validation
# =================================================================

# =================================================================
# FUTURE ROADMAP:
# 🔹 Real-time monitoring  🔹 SIEM integration  
# 🔹 Threat scoring       🔹 Email alerts
# =================================================================

# Connect: yuvaraj@cybersec.com | https://linkedin.com/in/yuvaraj-m-b718151b9
