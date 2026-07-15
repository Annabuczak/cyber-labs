#Scenario

#A small organisation needs a system to record and manage cybersecurity incidents.
# Staff can report incidents, analysts can investigate them, evidence can be added,
# and each case can move through different statuses until it is closed.

class Reporter:
    def __init__(self,name,email,password,department):
        self.name = name
        self.email = email
        self.password = password


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