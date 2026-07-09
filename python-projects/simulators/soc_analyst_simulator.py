severity_alert_list = ["Low", "Medium", "High", "Critical"]


class SecurityAlert:

    def __init__(self, username, IP_address, severity, description):
        self.username = username
        self.IP_address = IP_address
        self.severity = severity
        self.description = description

    def display_alert(self):
        print("\n--- Security Alert ---")
        print(f"User: {self.username}")
        print(f"IP: {self.IP_address}")
        print(f"Severity: {self.severity}")
        print(f"Description: {self.description}")

    def display_response(self):
        if self.severity == "Low":
            print("Response: Monitor alert")
        elif self.severity == "Medium":
            print("Response: Check with SOC2")
        elif self.severity == "High":
            print("Response: Check with SOC2 and SOC3")
        elif self.severity == "Critical":
            print("Response: Alert all teams")


alerts = []
running = True

while running:
    print("\nSOC Analyst Simulator")
    print("1. Add Alert")
    print("2. View Alerts")
    print("3. View High Risk Alerts")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Username: ")
        IP_address = input("IP address: ")
        severity = input("Severity (Low/Medium/High/Critical): ")
        description = input("Description: ")

        if severity in severity_alert_list:
            new_alert = SecurityAlert(username, IP_address, severity, description)
            alerts.append(new_alert)
            print("Alert added successfully")
        else:
            print("Invalid severity. Please use Low, Medium, High, or Critical.")

    elif choice == "2":
        if len(alerts) == 0:
            print("No alerts found")
        else:
            for alert in alerts:
                alert.display_alert()
                alert.display_response()

    elif choice == "3":
        found_high_risk = False

        for alert in alerts:
            if alert.severity == "High" or alert.severity == "Critical":
                alert.display_alert()
                alert.display_response()
                found_high_risk = True

        if not found_high_risk:
            print("No high risk alerts found")

    elif choice == "4":
        print("Exiting SOC Analyst Simulator")
        running = False

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
