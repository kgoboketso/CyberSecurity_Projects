import socket
from  datetime import datetime

target = input('Enter targer IP or domain:')

start_port = int(input("Enter start port: "))
End_port = int(input("Enter your End port: "))

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    # Resolve domain to IP
    target_ip = socket.gethostbyname(target)

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown service"

            print(f"[OPEN] Port {port} - {service}")

        s.close()

except socket.gaierror:
    print("Hostname could not be resolved")

except socket.error:
    print("Could not connect to server")

print("-" * 50)
print(f"Scanning compl
