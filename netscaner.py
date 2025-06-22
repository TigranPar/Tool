import socket
import sys

def scan_ports(ip, ports):
    print(f"\n[~] ip scanning: {ip}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            sock.connect((ip, port))
            print(f"[+] port open: {port}")
            sock.close()
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    target_ip = sys.argv[1]

    ports_to_scan = [
        20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 111, 123, 135, 137, 138, 139,
        143, 161, 162, 179, 389, 443, 445, 465, 512, 513, 514, 587, 636, 993, 995,
        1080, 1433, 1521, 1723, 2049, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 8888
    ]
    scan_ports(target_ip, ports_to_scan)
