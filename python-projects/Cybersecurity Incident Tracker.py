# Scenario

# A small organisation needs a system to record and manage cybersecurity incidents.
# Staff can report incidents, analysts can investigate them, evidence can be added,
# and each case can move through different statuses until it is closed.

class Reporter:
    def __init__(self, name, email, password, department):
        self.name = name
        self.email = email
        self.password = password


reporter_1 = Reporter(
    name="John",
    email="John@email.com",
    password="weakpassword12",
    department="SOC1"
)
reporter_2 = Reporter(
    name="Ben",
    email="ben@email",
    password="123234",
    department="SOC2"
)


class Analyst(Reporter):
    def __init__(self, name, email, password, department, skill_level):
        super().__init__(name, email, password, department)
        self.skill_level = skill_level


analyst_1 = Analyst(
    "Anna",
    "anna@email.com",
    "password123",
    "Cybersecurity",
    "Beginner"
)

analyst_2 = Analyst(
    "Louie",
    "Louie@.com",
    "password123",
    "Cybersecurity",
    "Mid"
)

analyst_3 = Analyst(
    "John",
    "John@.com",
    "password123",
    "Cybersecurity",
    "Senior"
)


class Incident:
    def __init__(self, incident_id, title, description, type, severity, status, reporter, analyst_assigned,
                 evidence_notes, ):
        self.incident_id = incident_id
        self.title = title
        self.description = description
        self.type = type
        self.severity = severity
        self.status = status
        self.reporter = reporter
        self.analyst_assigned = analyst_assigned
        self.evidence_notes = evidence_notes


incident_1 = Incident(
    "101",
    "Phishing emails"
    "Several emails sent from email resembling Microsoft domain"
    "Phishing"
    "Low"
    "Closed"
    "John"
    "Anna'"
    "None"

)
incident_2 = Incident(
    "102",
    "Bruteforce attack"
    "Several attempts to force entry to main server"
    "High"
    "Closed"
    "Ben"
    "John"
    "Senior"
    "None"
)