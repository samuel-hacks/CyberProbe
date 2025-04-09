import socket

def scan_ports(target_ip, ports = [21, 22, 23, 80, 443, 8080]):
    open_ports = []
    print(f"[+] Scanning {target_ip}...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((target_ip, port)) == 0:
                open_ports.append(port)
    return open_ports