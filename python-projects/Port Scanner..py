import socket

print(socket.gethostbyname("google.com"))

ip = socket.gethostbyname("google.com")
print(ip)

target = socket.gethostbyname("google.com")
print(target)

scanner = socket.socket()
print(scanner)

result = scanner.connect_ex((target, 443))
print(scanner)
print(result)

if result == 0:
    print("Port 443 is closed")
else:
    print("Port 443 is closed")

ports = [22, 80, 443]

for port in ports:
    scanner = socket.socket()

    result = scanner.connect_ex((target, port))

    if result == 0:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))

    scanner.close()







