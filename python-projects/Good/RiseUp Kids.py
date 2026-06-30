# RiseUp Kids app
import datetime

print("Welcome to RiseUp Kids")


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Behaviour:
    def __init__(self, name, category, reward_type, points):
        self.name = name
        self.category = category
        self.reward_type = reward_type
        self.points = points


# Children
child_1 = Child("Louie", 10)
child_2 = Child("Dotty", 10)

print(f"Hello, {child_1.name}'s parent!")
print(f"{child_1.name} is {child_1.age} years old.")
print(f"{child_2.name} is {child_2.age} years old.")


# Behaviours
bed_made = Behaviour("Bed made", "Responsibility", "Bonus", 2)
bedroom_tidy = Behaviour("Bedroom tidy", "Responsibility", "Bonus", 2)
buddy_walked = Behaviour("Buddy walked", "Responsibility", "Bonus", 5)
helped_mum_without_being_asked = Behaviour("Helped Mum without asking", "Kindness", "Bonus", 5)
takes_no_as_answer = Behaviour("Accepted 'No' first time", "Self-control", "Bonus", 4)
good_sportsmanship = Behaviour("Good sportsmanship", "Self-control", "Bonus", 5)
honest_about_mistakes = Behaviour("Honest about mistake", "Honesty", "Bonus", 5)
good_behaviour_mum_said_so = Behaviour("Good behaviour", "Kindness", "Bonus", 5)
apologies_sincerely = Behaviour("Apologised sincerely", "Kindness", "Bonus", 4)
included_another_child = Behaviour("Included another child", "Kindness", "Bonus", 4)
control_frustration = Behaviour("Controlled frustration", "Self-control", "Bonus", 8)

bed_not_made = Behaviour("Bed not made", "Responsibility", "Deduction", -2)
bedroom_messy = Behaviour("Bedroom messy", "Responsibility", "Deduction", -3)
clothes_on_bathroom_floor = Behaviour("Clothes on bathroom floor", "Responsibility", "Deduction", -2)
shoes_left_in_hallway = Behaviour("Shoes left in hallway", "Responsibility", "Deduction", -1)
plate_left_upstairs = Behaviour("Plate left upstairs", "Responsibility", "Deduction", -2)
didnt_clean_after_eating = Behaviour("Didn't clean after eating", "Responsibility", "Deduction", -2)
didnt_walk_buddy_when_asked = Behaviour("Didn't walk Buddy when asked", "Responsibility", "Deduction", -3)
didnt_complete_chore = Behaviour("Didn't complete chore", "Responsibility", "Deduction", -4)

talking_back = Behaviour("Talking back", "Respect", "Deduction", -3)
swearing = Behaviour("Swearing", "Respect", "Deduction", -3)
slamming_door = Behaviour("Slamming door", "Respect", "Deduction", -3)
ignored_instruction = Behaviour("Ignored instruction", "Respect", "Deduction", -3)
asked_again_after_no = Behaviour("Asked again after 'No'", "Respect", "Deduction", -1)
begged_for_youtube = Behaviour("Begged for YouTube", "Respect", "Deduction", -2)
begged_for_phone = Behaviour("Begged for phone", "Respect", "Deduction", -2)
begged_for_computer = Behaviour("Begged for computer", "Respect", "Deduction", -2)
asked_for_tesco_money_after_refusing_chores = Behaviour("Asked for Tesco money after refusing chores", "Respect", "Deduction", -4)

poor_sportsmanship = Behaviour("Poor sportsmanship", "Kindness", "Deduction", -5)
threatened_another_child = Behaviour("Threatened another child", "Kindness", "Deduction", -8)
deliberately_rude = Behaviour("Deliberately rude", "Kindness", "Deduction", -5)
took_frustration_out_on_buddy = Behaviour("Took frustration out on Buddy", "Kindness", "Deduction", -5)
refused_to_apologise = Behaviour("Refused to apologise", "Kindness", "Deduction", -4)


class DailyLog:
    def __init__(self, date, child, recorded_behaviours, daily_score, notes):
        self.date = date
        self.child = child
        self.recorded_behaviours = recorded_behaviours
        self.daily_score = daily_score
        self.notes = notes

    def calculate_daily_score(self):
        total = 0

        for behaviour in self.recorded_behaviours:
            total += behaviour.points

        self.daily_score = total
        return total

    def add_behaviour(self, behaviour):
        self.recorded_behaviours.append(behaviour)
        self.calculate_daily_score()

    def show_summary(self):
        print(f"\nDaily log for {self.child.name}")
        print(f"Date: {self.date}")
        print("\nBehaviours:")

        for behaviour in self.recorded_behaviours:
            print(f"- {behaviour.name}: {behaviour.points:+}")

        print(f"\nDaily Score: {self.daily_score:+}")

        if self.notes:
            print(f"Notes: {self.notes}")


today_log = DailyLog(
    date=datetime.date.today(),
    child=child_1,
    recorded_behaviours=[bed_made, bedroom_tidy, talking_back],
    daily_score=0,
    notes="Good effort today."
)

today_log.calculate_daily_score()
today_log.show_summary()

class WeeklySummary:
    def __init__(self,week_number, week_score,reward_level,mum_notes,date,child, recorded_behaviours):

        self.week_number = week_number
        self.week_score = week_score
        self.reward = reward_level
        self.mum_notes = mum_notes
        self.date = date
        self.child = child
        self.recorded_behaviours = recorded_behaviours

    def calculate_average_score(self):
        total = 0

        for behaviour in self.behaviour:
            total += behaviour.points

        self.week_score = total
        return total

    def reward_level(self):



week_log = WeeklySummary(
    date=datetime.date.today(),
    week_number=1,
    reward_level=1,
    child=child_1,
    recorded_behaviours=[bed_made, bedroom_tidy, talking_back],
    week_score=0,
    mum_notes="Good effort today.",
)
reward_levels = [
    {"min": 95, "max": 110, "reward": "Family Adventure"},
    {"min": 85, "max": 94, "reward": "Extra Nintendo / Choose Dinner"},
    {"min": 70, "max": 84, "reward": "Normal Privileges"},
    {"min": 50, "max": 69, "reward": "Reduced Screens"},
    {"min": 0, "max": 49, "reward": "Rebuild Week"},
]