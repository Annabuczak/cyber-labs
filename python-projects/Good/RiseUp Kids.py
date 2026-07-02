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

reward_levels = [
    {"min": 0, "max": 49, "reward": "No weekly reward yet"},
    {"min": 50, "max": 74, "reward": "Tesco snack"},
    {"min": 75, "max": 99, "reward": "Bikes with Mum"},
    {"min": 100, "max": 100, "reward": "Choose Friday dinner"},
]


class RewardManager:
    def __init__(self, reward_levels):
        self.reward_levels = reward_levels
        self.current_reward = "No reward"

    def determine_reward(self, weekly_score):
        if weekly_score >= 100:
            self.current_reward = "Choose Friday dinner"
        elif weekly_score >= 75:
            self.current_reward = "Bikes with Mum"
        elif weekly_score >= 50:
            self.current_reward = "Tesco snack"
        else:
            self.current_reward = "No weekly reward yet"

        return self.current_reward

    def unlock_reward(self, child, weekly_score):
        reward = self.determine_reward(weekly_score)

        if weekly_score >= 50:
            print(f"Congratulations! {child.name} unlocked: {reward}")
        else:
            print(f"{child.name} has not unlocked a reward yet.")

    def show_rewards(self):
        print("\n===== Rewards =====")

        for level in self.reward_levels:
            print(f"{level['min']} - {level['max']} XP: {level['reward']}")

reward_manager = RewardManager(reward_levels)


class WeeklySummary:
    def __init__(self, week_number, mum_notes, child, daily_logs):
        self.week_number = week_number
        self.mum_notes = mum_notes
        self.child = child
        self.daily_logs = daily_logs

        self.weekly_score = self.calculate_weekly_score()
        self.reward = self.get_weekly_reward()

    def calculate_weekly_score(self):
        total = 0

        for log in self.daily_logs:
            total += log.daily_score

        if total < 0:
            total = 0

        if total > 100:
            total = 100

        return total

    def determine_reward(self):
        if self.weekly_score >= 100:
            return "Choose Friday dinner"
        elif self.weekly_score >= 75:
            return "Bikes with Mum"
        elif self.weekly_score >= 50:
            return "Tesco snack"
        else:
            return "No weekly reward yet"

    def get_weekly_reward(self):
        return self.determine_reward()

    def show_summary(self):
        print("\n===== Weekly Summary =====")
        print(f"Child: {self.child.name}")
        print(f"Week: {self.week_number}")
        print(f"Weekly XP: {self.weekly_score}")
        print(f"Reward: {self.reward}")

        print("\nDaily Scores:")
        for log in self.daily_logs:
            print(f"{log.date}: {log.daily_score:+}")

        if self.mum_notes:
            print(f"\nMum's Notes: {self.mum_notes}")

monday = DailyLog(
    date=datetime.date(2026, 7, 6),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

tuesday = DailyLog(
    date=datetime.date(2026, 7, 7),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

wednesday = DailyLog(
    date=datetime.date(2026, 7, 8),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

thursday = DailyLog(
    date=datetime.date(2026, 7, 9),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

friday = DailyLog(
    date=datetime.date(2026, 7, 10),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

saturday = DailyLog(
    date=datetime.date(2026, 7, 11),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

sunday = DailyLog(
    date=datetime.date(2026, 7, 12),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)


week_1 = WeeklySummary(
    week_number=1,
    child=child_1,
    daily_logs=[monday, tuesday, wednesday, thursday, friday, saturday, sunday],
    mum_notes="Much calmer this week."
)

week_1.show_summary()

class BehaviourCatalogue:
    def __init__(self, behaviours):
        self.behaviours = behaviours

    def show_behaviour_list(self):
        print("\n===== Behaviour Catalogue =====")

        for behaviour in self.behaviours:
            print(f"{behaviour.name} | {behaviour.category} | {behaviour.reward_type} | {behaviour.points:+}")

    def find_behaviour(self, behaviour_name):
        for behaviour in self.behaviours:
            if behaviour.name.lower() == behaviour_name.lower():
                return behaviour

        return None

    def list_bonus_behaviours(self):
        print("\n===== Bonus Behaviours =====")

        for behaviour in self.behaviours:
            if behaviour.reward_type == "Bonus":
                print(f"{behaviour.name}: {behaviour.points:+}")

    def list_deduction_behaviours(self):
        print("\n===== Deduction Behaviours =====")

        for behaviour in self.behaviours:
            if behaviour.reward_type == "Deduction":
                print(f"{behaviour.name}: {behaviour.points:+}")

    def add_behaviour(self, behaviour):
        self.behaviours.append(behaviour)

    def remove_behaviour(self, behaviour_name):
        behaviour = self.find_behaviour(behaviour_name)

        if behaviour:
            self.behaviours.remove(behaviour)
            print(f"{behaviour.name} removed.")
        else:
            print("Behaviour not found.")

behaviour_catalogue = BehaviourCatalogue([
    bed_made,
    bedroom_tidy,
    buddy_walked,
    helped_mum_without_being_asked,
    takes_no_as_answer,
    good_sportsmanship,
    honest_about_mistakes,
    good_behaviour_mum_said_so,
    apologies_sincerely,
    included_another_child,
    control_frustration,
    bed_not_made,
    bedroom_messy,
    clothes_on_bathroom_floor,
    shoes_left_in_hallway,
    plate_left_upstairs,
    didnt_clean_after_eating,
    didnt_walk_buddy_when_asked,
    didnt_complete_chore,
    talking_back,
    swearing,
    slamming_door,
    ignored_instruction,
    asked_again_after_no,
    begged_for_youtube,
    begged_for_phone,
    begged_for_computer,
    asked_for_tesco_money_after_refusing_chores,
    poor_sportsmanship,
    threatened_another_child,
    deliberately_rude,
    took_frustration_out_on_buddy,
    refused_to_apologise,
])