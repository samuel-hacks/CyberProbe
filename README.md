# CyberProbe

**CyberProbe** is a modular cybersecurity toolkit written in Python, designed to demonstrate and simulate two commonly used techniques in cyberattacks:

- Keylogging
- Port Scanning

Built as part of a second-year project for System Security Management, CyberProbe helps learners, researchers, and ethical hackers explore how attackers operate, and what kinds of weaknesses exist in unsecured systems.


## Background: Why These Techniques?

Both **keylogging** and **port scanning** are foundational tools used by cybercriminals and penetration testers.

| Technique      | Purpose                                      | Common Usage               |
|----------------|----------------------------------------------|----------------------------|
| Keylogging     | Steal user input (credentials, messages)     | Credential theft, spyware |
| Port Scanning  | Find open network services                   | Reconnaissance             |

By simulating these tools, defenders and students can:

- Understand attacker workflows
- Recognize system vulnerabilities
- Test defenses (like firewalls, IDS, sandboxing)

---

## Project Directory Structure

CyberProbe/

│

├── keylogger.py         # Captures all keyboard inputs

├── port_scanner.py      # Scans IPs for open ports

├── requirements.txt     # Python dependencies

├── README.md            # Project documentation

└── keylog.txt              # Auto-generated keylogger output file


---

## 1) Keylogger Module

### Definition

A keylogger is a surveillance tool that records every keystroke typed on a device. Malicious actors use them to capture:

- Usernames/passwords
- Credit card numbers
- Personal messages

### How It Works

- Uses the `pynput` library to hook into keyboard events
- Listens for each `on_press` event and appends it to a buffer
- Stores results into a local file (`log.txt`)

### Security Insight

> In a real-world system, keyloggers are often installed by malware or delivered through phishing. Some run in stealth mode or even load into kernel space.

### How to Defend Against Keyloggers

- Use endpoint detection tools (like OSSEC or Wazuh)
- Implement behavioral detection (e.g., multiple failed logins + keylogging signals)
- Limit user permissions and use sandboxing

---

## 2) Port Scanner Module

### Definition

Port scanning is used to **map a system’s attack surface**. It identifies which ports are open and what services may be running on them.

For example:
- **Port 22** ➝ SSH  
- **Port 80** ➝ HTTP  
- **Port 443** ➝ HTTPS  

### How It Works

- Uses Python’s `socket` library
- Attempts to `connect_ex()` to each port in the range `1–1024`
- If the connection is successful, the port is marked as **OPEN**

### What It Tells You

- **Open ports** = Possible entry points for attackers  
- **Closed ports** = No service OR filtered by firewall  
- **Repeated scans** from same IP = Possible reconnaissance or attack

### Defense Against Port Scanning

- Use **firewalls** to block unused ports
- Enable **port knocking** or **IP whitelisting**
- Use **port scan detection tools** like:
  - 🔎 Snort
  - 🔒 Fail2Ban
  - 🛡️ Suricata

---

## Requirements

- Python 3.8 or higher  
- Pip (Python package manager)  

---

## Learning Outcomes

By using **CyberProbe**, learners will:

- Understand attacker methods for reconnaissance and surveillance  
- Gain hands-on experience writing real-world security tools in Python  
- Practice safe cybersecurity operations in a controlled lab environment  
- Improve awareness of system vulnerabilities and hardening techniques
  
---

## Future Enhancements

Here’s what could be added in future versions of CyberProbe:

- Real-time alerts when keylog events are detected  
- GUI interface using Tkinter or PyQt  
- Encrypted keystroke logging for secure forensic review  
- Timing-based port scan detection to simulate Snort-style rule triggers  

---


