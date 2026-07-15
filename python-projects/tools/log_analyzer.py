from pathlib import Path


log_path = Path(__file__).resolve().parents[1] / "sample-logs" / "server.log"

with open(log_path, "r") as file:
    logs = file.readlines()



#Failed logins

failed_logins = 0

for line in logs:
    line = line.strip()

    if "Failed login" in line:
        failed_logins +=1

print("Failed logins:", failed_logins,)

#ERRORS

error_logins = 0
for line in logs:
    line = line.strip()
    if "ERROR" in line:
        error_logins += 1
        print("Error logins:", error_logins,)

#WARNING

warning_logins = 0
for line in logs:
    line = line.strip()
    if "WARNING" in line:
        warning_logins += 1
print("Warning logins:", warning_logins,)

#INFO
info_logins = 0
for line in logs:
    line = line.strip()
    if "INFO" in line:
        info_logins += 1

if failed_logins >= 2:
   print("ALERT: Multiple failed login attempts detected!")

print("\nLog Analysis Report")
print("-------------------")
print("Failed logins:", failed_logins)
print("Errors:", error_logins)
print("Warnings:", warning_logins)
print("Info messages:", info_logins)
