import socket

target = socket.gethostbyname("bbc.co.uk")
print("Target IP:", target)

scanner = socket.socket()
result = scanner.connect_ex((target, 443))

if result == 0:
    print("Port 443 is open")
else:
    print("Port 443 is closed")

scanner.close()

ports = [22, 80, 443]

for port in ports:
    scanner = socket.socket()
    scanner.settimeout(3)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))

    scanner.close()







