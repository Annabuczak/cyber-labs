ip = "123.33.44"
print(ip)


ip = "123.33.44"
parts = ip.split(".")
print(parts)
ip = "123.33.44"

parts = ip.split(".")
print(len(parts))

if len(parts) == 3:
    print("IP is valid")
else:
    print("IP is not valid")

