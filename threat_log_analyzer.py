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
