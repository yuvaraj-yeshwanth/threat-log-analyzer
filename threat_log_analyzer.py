import re
import sys
import json

def parse_logs(file_path):
    try:
        with open(file_path, 'r') as f:
            logs = f.readlines()
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
        return []
    
    threats = []
    pattern = re.compile(r'failed|unauthorized|error|intrusion|malware|attack', re.IGNORECASE)

    for log in logs:
        if pattern.search(log):
            threats.append(log.strip())

    return threats

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Usage: python3 threat_log_analyzer.py <log_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    threats_found = parse_logs(file_path)

    if threats_found:
        print("\n🚨 Potential Threats Found:")
        for threat in threats_found:
            print(threat)

        # Save detected threats to a file
        with open("threats_found.json", "w") as json_file:
            json.dump(threats_found, json_file, indent=4)
        print("\n✅ Threats saved to 'threats_found.json'")
    else:
        print("✅ No threats detected.") 
