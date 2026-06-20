with open("server.log", "r") as file:
    logs = file.readlines()

with open("server.log", "r") as file:
    logs = file.readlines()

failed_logins = 0

for line in logs:
    line = line.strip()

    if "Failed login" in line:
        failed_logins += 1

print("Failed logins:", failed_logins)

for line in logs:

    print(repr(line))

print(logs)

for line in logs:

    print(line)