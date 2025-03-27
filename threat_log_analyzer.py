"""
Threat Log Analyzer
Author: Yuvaraj M
Description: Enterprise-grade log analysis tool for SOC teams
Version: 1.1
"""

import re
import sys
import json
from typing import List, Pattern
from pathlib import Path

# MITRE ATT&CK aligned detection patterns
THREAT_PATTERNS = [
    r'failed', r'unauthorized', r'error',
    r'intrusion', r'malware', r'attack',
    r'breach', r'exploit', r'injection'
]

class ThreatAnalyzer:
    """Core log analysis engine with enterprise security patterns"""
    
    def __init__(self, patterns: List[str] = THREAT_PATTERNS):
        self.threat_regex: Pattern = re.compile(
            '|'.join(patterns),
            re.IGNORECASE
        )
    
    def analyze(self, log_path: str) -> List[str]:
        """
        Perform threat analysis on log files
        
        Args:
            log_path: Path to log file
            
        Returns:
            List of matched threat entries
        """
        try:
            log_file = Path(log_path)
            if not log_file.exists():
                raise FileNotFoundError(f"Log file not found: {log_path}")
                
            with log_file.open('r', encoding='utf-8') as f:
                return [
                    line.strip() for line in f
                    if self.threat_regex.search(line)
                ]
                
        except (IOError, PermissionError) as e:
            print(f"[ANALYSIS ERROR] {str(e)}")
            return []

def generate_report(threats: List[str], report_path: str = "threats_found.json"):
    """
    Generate JSON threat report
    
    Args:
        threats: List of detected threat entries
        report_path: Output report path
    """
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump({
                "meta": {
                    "system": "Threat Log Analyzer",
                    "version": "1.1",
                    "detected_threats": len(threats)
                },
                "findings": threats
            }, f, indent=2)
            
        print(f"Report generated: {report_path}")
        
    except IOError as e:
        print(f"[REPORT ERROR] Failed to save report: {str(e)}")

def main():
    """Command line interface for threat analysis"""
    if len(sys.argv) != 2:
        print("Usage: threat_analyzer.py <log_file_path>")
        print("Example: threat_analyzer.py /var/log/secure.log")
        sys.exit(1)
        
    analyzer = ThreatAnalyzer()
    detected = analyzer.analyze(sys.argv[1])
    
    if detected:
        print(f"\n🔍 Detected {len(detected)} potential threats:")
        for idx, threat in enumerate(detected, 1):
            print(f"{idx}. {threat}")
            
        generate_report(detected)
        sys.exit(0)
    else:
        print("✅ No security threats detected")
        sys.exit(0)

if __name__ == "__main__":
    main()
