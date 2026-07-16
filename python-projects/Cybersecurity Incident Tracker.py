class Person:
    def __init__(self, name, email, department):
        self.name = name
        self.email = email
        self.department = department


class Reporter(Person):
    pass


class Analyst(Person):
    def __init__(self, name, email, department, skill_level):
        super().__init__(name, email, department)
        self.skill_level = skill_level


class Incident:
    def __init__(
        self,
        incident_id,
        title,
        description,
        incident_type,
        severity,
        status,
        reporter,
        analyst_assigned,
        evidence_notes
    ):
        self.incident_id = incident_id
        self.title = title
        self.description = description
        self.incident_type = incident_type
        self.severity = severity
        self.status = status
        self.reporter = reporter
        self.analyst_assigned = analyst_assigned
        self.evidence_notes = evidence_notes


class IncidentTracker:
    def __init__(self):
        self.incidents = []

    def add_incident(self, incident):
        self.incidents.append(incident)

    def show_incidents(self):
        for incident in self.incidents:
            print(f"ID: {incident.incident_id}")
            print(f"Title: {incident.title}")
            print(f"Description: {incident.description}")
            print(f"Type: {incident.incident_type}")
            print(f"Severity: {incident.severity}")
            print(f"Status: {incident.status}")
            print(f"Reporter: {incident.reporter.name}")
            print(f"Analyst: {incident.analyst_assigned.name}")
            print(f"Evidence: {incident.evidence_notes}")
            print()

    def show_open_incidents(self):
        for incident in self.incidents:
            if incident.status == "Open":
                print(f"Open incident: {incident.incident_id} - {incident.title}")

    def show_closed_incidents(self):
        for incident in self.incidents:
            if incident.status == "Closed":
                print(f"Closed incident: {incident.incident_id} - {incident.title}")


    def show_severity(self):
        for incident in self.incidents:
            if incident.severity == "Low":
                print(f"Incident severity Low:{incident.incident_id} - {incident.severity} ")
            elif incident.severity == "Medium":
                print(f"Incident severity Medium: {incident.incident_id} - {incident.severity} ")
            elif incident.severity == "High":
                print(f"Incident severity High: {incident.incident_id} - {incident.severity} ")



class Response:
    def __init__(self,severity,status):
        self.severity = severity
        self.status = status

    def response_plan (self):
        for response in self.response_plan:
            if response.status == "Open":
                response.severity = "Low"
                print(f" Response plan: {response.incident_id} - {response.title}")

response_1 = Response("Low", "Open")
response_2 = Response("Medium", "Open")
response_3 = Response("High", "Open")


reporter_1 = Reporter("John", "john@email.com", "SOC1")
reporter_2 = Reporter("Ben", "ben@email.com", "SOC2")

analyst_1 = Analyst("Anna", "anna@email.com", "Cybersecurity", "Beginner")
analyst_3 = Analyst("John", "john.analyst@email.com", "Cybersecurity", "Senior")

incident_1 = Incident(
    "101",
    "Phishing emails",
    "Several emails were sent from an address resembling a Microsoft domain.",
    "Phishing",
    "Low",
    "Open",
    reporter_1,
    analyst_1,
    []
)

incident_2 = Incident(
    "102",
    "Brute-force attack",
    "Several attempts were made to gain access to the main server.",
    "Unauthorised Access",
    "High",
    "Closed",
    reporter_2,
    analyst_3,
    []
)

incident_tracker = IncidentTracker()
incident_tracker.add_incident(incident_1)
incident_tracker.add_incident(incident_2)


incident_tracker.show_incidents()
incident_tracker.show_open_incidents()
incident_tracker.show_severity()
incident_tracker.show_closed_incidents()

response = Response(severity="Low", status="Open")
incident_tracker.add_incident(response)
response_1.response_plan()
incident_tracker.show_incidents()
response_1.response_plan()
