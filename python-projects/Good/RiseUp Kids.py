# RiseUp Kids app
import csv
import datetime
import sys
import json
import os

print("Welcome to RiseUp Kids")


DATA_FILE = os.path.join(os.path.dirname(__file__), "riseup_data.json")


def get_monday_for_date(date):
    return date - datetime.timedelta(days=date.weekday())


def date_from_text(date_text):
    return datetime.datetime.strptime(date_text, "%Y-%m-%d").date()


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    return {"accounts": []}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def account_key(account, child):
    return f"{account.email.lower()}-{child.name.lower()}"


def default_account_data():
    return {
        "name": "Anna",
        "email": "buczakanna@gmail.com",
        "pin": "1234",
        "child": {
            "name": "Louie",
            "age": 10
        },
        "custom_behaviours": [],
        "current_week_start": str(get_monday_for_date(datetime.date.today())),
        "past_weeks": [],
        "weekly_logs": {}
    }


def get_saved_accounts():
    data = load_data()
    accounts = data["accounts"]

    anna_exists = False

    for saved_account in accounts:
        if saved_account["email"] == "buczakanna@gmail.com" and saved_account["child"]["name"] == "Louie":
            anna_exists = True

    if not anna_exists:
        accounts.insert(0, default_account_data())

    return accounts


def save_new_account(account, child):
    data = load_data()

    for saved_account in data["accounts"]:
        same_email = saved_account["email"].lower() == account.email.lower()
        same_child = saved_account["child"]["name"].lower() == child.name.lower()

        if same_email and same_child:
            return saved_account

    saved_account = {
        "name": account.name,
        "email": account.email,
        "pin": account.pin,
        "child": {
            "name": child.name,
            "age": child.age
        },
        "custom_behaviours": [],
        "current_week_start": str(get_monday_for_date(datetime.date.today())),
        "past_weeks": [],
        "weekly_logs": {}
    }
    data["accounts"].append(saved_account)
    save_data(data)
    return saved_account




class UserAccount:
    def __init__(self, name, email, pin):
        self.name = name
        self.email = email
        self.pin = pin


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def check_pin(correct_pin):
    attempts_left = 3

    while attempts_left > 0:
        user_pin = input("Please enter your PIN: ")

        if user_pin == correct_pin:
            print("Access granted.")
            return

        attempts_left -= 1
        print("Incorrect PIN.")

        if attempts_left == 0:
            print("Please change your PIN.")
            sys.exit()


def create_new_account():
    parent_name = input("Parent name: ")
    email = input("Email: ")
    pin = input("Create a PIN: ")
    child_name = input("Child name: ")
    child_age = input("Child age: ")

    if child_age.isdigit():
        child_age = int(child_age)
    else:
        child_age = 0

    new_account = UserAccount(parent_name, email, pin)
    new_child = Child(child_name, child_age)
    save_new_account(new_account, new_child)
    print(f"Account created for {new_account.name}.")
    return new_account, new_child


def choose_account():
    while True:
        saved_accounts = get_saved_accounts()
        print("\n===== Account =====")

        for index, saved_account in enumerate(saved_accounts, start=1):
            child_name = saved_account["child"]["name"]
            print(f"{index}. Log into {saved_account['name']}'s account ({child_name})")

        create_account_choice = len(saved_accounts) + 1
        print(f"{create_account_choice}. Create new account")

        account_choice = input("Enter your choice: ")

        if account_choice.isdigit():
            account_index = int(account_choice) - 1
        else:
            print("Invalid choice. Please try again.")
            continue

        if 0 <= account_index < len(saved_accounts):
            saved_account = saved_accounts[account_index]
            existing_account = UserAccount(saved_account["name"], saved_account["email"], saved_account["pin"])
            existing_child = Child(saved_account["child"]["name"], saved_account["child"]["age"])
            check_pin(existing_account.pin)
            return existing_account, existing_child, saved_account
        elif int(account_choice) == create_account_choice:
            new_account, new_child = create_new_account()
            return new_account, new_child, None
        else:
            print("Invalid choice. Please try again.")


class Behaviour:
    def __init__(self, name, category, reward_type, points):
        self.name = name
        self.category = category
        self.reward_type = reward_type
        self.points = points

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "reward_type": self.reward_type,
            "points": self.points
        }


account, child_1, selected_saved_account = choose_account()

print(f"Hello, {account.name}!")
print(f"{child_1.name} is {child_1.age} years old.")


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

    def add_note(self, note):
        self.notes = note

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
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

reward_levels = [
    {"min": 0, "max": 9, "reward": "No weekly reward yet"},
    {"min": 10, "max": 19, "reward": "Tesco snack"},
    {"min": 20, "max": 34, "reward": "Bikes with Mum"},
    {"min": 35, "max": 100, "reward": "Choose Friday dinner"},
]


class RewardManager:
    def __init__(self, reward_levels):
        self.reward_levels = reward_levels
        self.current_reward = "No reward"

    def determine_reward(self, weekly_score):
        if weekly_score >= 35:
            self.current_reward = "Choose Friday dinner"
        elif weekly_score >= 20:
            self.current_reward = "Bikes with Mum"
        elif weekly_score >= 10:
            self.current_reward = "Tesco snack"
        else:
            self.current_reward = "No weekly reward yet"

        return self.current_reward

    def unlock_reward(self, child, weekly_score):
        reward = self.determine_reward(weekly_score)

        if weekly_score >= 10:
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

    def refresh(self):
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
        if self.weekly_score >= 35:
            return "Choose Friday dinner"
        elif self.weekly_score >= 20:
            return "Bikes with Mum"
        elif self.weekly_score >= 10:
            return "Tesco snack"
        else:
            return "No weekly reward yet"

    def get_weekly_reward(self):
        return self.determine_reward()

    def calculate_weekly_average(self):
        if len(self.daily_logs) == 0:
            return 0

        return self.weekly_score / len(self.daily_logs)

    def show_progress_graph(self):
        print("\n===== Progress Graph =====")

        for log in self.daily_logs:
            bar = "#" * max(log.daily_score, 0)
            print(f"{log.date}: {bar} {log.daily_score:+}")

    def export_history(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "child", "daily_score", "notes", "behaviours"])

            for log in self.daily_logs:
                behaviour_names = []

                for behaviour in log.recorded_behaviours:
                    behaviour_names.append(behaviour.name)

                writer.writerow([
                    log.date,
                    log.child.name,
                    log.daily_score,
                    log.notes,
                    ", ".join(behaviour_names)
                ])

        print(f"History exported to {filename}")

    def show_summary(self):
        print("\n===== Weekly Summary =====")
        print(f"Child: {self.child.name}")
        print(f"Week: {self.week_number}")
        print(f"Weekly XP: {self.weekly_score}")
        print(f"Reward: {self.reward}")
        print(f"Weekly Average: {self.calculate_weekly_average():.1f}")

        print("\nDaily Scores:")
        for log in self.daily_logs:
            print(f"{log.date}: {log.daily_score:+}")

        if self.mum_notes:
            print(f"\nMum's Notes: {self.mum_notes}")

if selected_saved_account and "current_week_start" in selected_saved_account:
    current_week_start = date_from_text(selected_saved_account["current_week_start"])
else:
    current_week_start = get_monday_for_date(datetime.date.today())


monday = DailyLog(
    date=current_week_start,
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

tuesday = DailyLog(
    date=current_week_start + datetime.timedelta(days=1),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

wednesday = DailyLog(
    date=current_week_start + datetime.timedelta(days=2),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

thursday = DailyLog(
    date=current_week_start + datetime.timedelta(days=3),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

friday = DailyLog(
    date=current_week_start + datetime.timedelta(days=4),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

saturday = DailyLog(
    date=current_week_start + datetime.timedelta(days=5),
    child=child_1,
    recorded_behaviours=[],
    daily_score=0,
    notes=""
)

sunday = DailyLog(
    date=current_week_start + datetime.timedelta(days=6),
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

    def get_behaviours_by_type(self, reward_type):
        matching_behaviours = []

        for behaviour in self.behaviours:
            if behaviour.reward_type == reward_type:
                matching_behaviours.append(behaviour)

        return matching_behaviours

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
        existing_behaviour = self.find_behaviour(behaviour.name)

        if existing_behaviour:
            print("That behaviour already exists.")
            return False

        self.behaviours.append(behaviour)
        return True

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

weekly_logs = {
    "monday": monday,
    "tuesday": tuesday,
    "wednesday": wednesday,
    "thursday": thursday,
    "friday": friday,
    "saturday": saturday,
    "sunday": sunday,
}


def set_week_dates(week_start):
    global current_week_start
    current_week_start = week_start

    for index, log in enumerate(weekly_logs.values()):
        log.date = current_week_start + datetime.timedelta(days=index)


def clear_current_week(week_start):
    set_week_dates(week_start)

    for log in weekly_logs.values():
        log.recorded_behaviours = []
        log.daily_score = 0
        log.notes = ""

    week_1.refresh()


def get_current_account_data(data):
    current_key = account_key(account, child_1)

    for saved_account in data["accounts"]:
        saved_child = Child(saved_account["child"]["name"], saved_account["child"]["age"])
        saved_user = UserAccount(saved_account["name"], saved_account["email"], saved_account["pin"])

        if account_key(saved_user, saved_child) == current_key:
            return saved_account

    return None


def create_week_snapshot():
    week_1.refresh()
    daily_logs = {}

    for day_name, log in weekly_logs.items():
        behaviour_names = []

        for behaviour in log.recorded_behaviours:
            behaviour_names.append(behaviour.name)

        daily_logs[day_name] = {
            "date": str(log.date),
            "score": log.daily_score,
            "notes": log.notes,
            "behaviours": behaviour_names
        }

    return {
        "week_start": str(current_week_start),
        "week_end": str(current_week_start + datetime.timedelta(days=6)),
        "weekly_score": week_1.weekly_score,
        "reward": week_1.reward,
        "daily_logs": daily_logs
    }


def save_app_data():
    data = load_data()
    saved_account = get_current_account_data(data)

    if saved_account is None:
        saved_account = {
            "name": account.name,
            "email": account.email,
            "pin": account.pin,
            "child": {
                "name": child_1.name,
                "age": child_1.age
            },
            "custom_behaviours": [],
            "current_week_start": str(current_week_start),
            "past_weeks": [],
            "weekly_logs": {}
        }
        data["accounts"].append(saved_account)

    custom_behaviours = []

    for behaviour in behaviour_catalogue.behaviours:
        custom_marker = getattr(behaviour, "custom", False)

        if custom_marker:
            custom_behaviours.append(behaviour.to_dict())

    saved_account["custom_behaviours"] = custom_behaviours
    saved_account["current_week_start"] = str(current_week_start)
    saved_account.setdefault("past_weeks", [])
    saved_account["weekly_logs"] = {}

    for day_name, log in weekly_logs.items():
        behaviour_names = []

        for behaviour in log.recorded_behaviours:
            behaviour_names.append(behaviour.name)

        saved_account["weekly_logs"][day_name] = {
            "notes": log.notes,
            "behaviours": behaviour_names
        }

    save_data(data)
    print("Saved.")


def load_custom_behaviours():
    data = load_data()
    saved_account = get_current_account_data(data)

    if saved_account is None:
        return

    for saved_behaviour in saved_account.get("custom_behaviours", []):
        behaviour = Behaviour(
            saved_behaviour["name"],
            saved_behaviour["category"],
            saved_behaviour["reward_type"],
            saved_behaviour["points"]
        )
        behaviour.custom = True
        behaviour_catalogue.add_behaviour(behaviour)


def load_weekly_logs():
    data = load_data()
    saved_account = get_current_account_data(data)

    if saved_account is None:
        return

    saved_week_start = saved_account.get("current_week_start")

    if saved_week_start:
        set_week_dates(date_from_text(saved_week_start))

    saved_weekly_logs = saved_account.get("weekly_logs", {})

    for day_name, saved_log in saved_weekly_logs.items():
        if day_name in weekly_logs:
            log = weekly_logs[day_name]
            log.notes = saved_log.get("notes", "")
            log.recorded_behaviours = []

            for behaviour_name in saved_log.get("behaviours", []):
                behaviour = behaviour_catalogue.find_behaviour(behaviour_name)

                if behaviour:
                    log.recorded_behaviours.append(behaviour)

            log.calculate_daily_score()

    week_1.refresh()


load_custom_behaviours()
load_weekly_logs()


def check_for_new_week():
    data = load_data()
    saved_account = get_current_account_data(data)

    if saved_account is None:
        save_app_data()
        return

    today_week_start = get_monday_for_date(datetime.date.today())

    if current_week_start >= today_week_start:
        return

    print("\nA new week has started.")
    print(f"Current saved week: {current_week_start} to {current_week_start + datetime.timedelta(days=6)}")
    print(f"This week starts: {today_week_start}")
    print("1. Save old week and start a fresh week")
    print("2. Keep working on the old week for now")

    reset_choice = input("Enter your choice: ")

    if reset_choice == "1":
        saved_account.setdefault("past_weeks", [])
        saved_account["past_weeks"].append(create_week_snapshot())
        save_data(data)
        clear_current_week(today_week_start)
        save_app_data()
        print("New week started.")
    else:
        print("Keeping the old week for now.")


check_for_new_week()


def choose_day():
    print("\nDays:")

    for day_name in weekly_logs:
        print(f"- {day_name}")

    day_choice = input("Choose a day: ").lower()

    if day_choice in weekly_logs:
        return weekly_logs[day_choice]

    print("Day not found.")
    return None


def add_behaviour_to_day():
    log = choose_day()

    if log is None:
        return

    while True:
        print("\nWhat do you want to add?")
        print("1. Bonus points")
        print("2. Deduct points")
        print("3. Show all behaviours")
        print("4. Done")

        behaviour_type_choice = input("Enter your choice: ")

        if behaviour_type_choice == "1":
            behaviours = behaviour_catalogue.get_behaviours_by_type("Bonus")
        elif behaviour_type_choice == "2":
            behaviours = behaviour_catalogue.get_behaviours_by_type("Deduction")
        elif behaviour_type_choice == "3":
            behaviours = behaviour_catalogue.behaviours
        elif behaviour_type_choice == "4":
            print("Finished recording behaviours.")
            break
        else:
            print("Invalid choice.")
            continue

        print("\nChoose a behaviour:")

        for index, behaviour in enumerate(behaviours, start=1):
            print(f"{index}. {behaviour.name} ({behaviour.points:+})")

        print("0. Back")
        behaviour_choice = input("Enter behaviour number: ")

        if behaviour_choice == "0":
            continue

        if not behaviour_choice.isdigit():
            print("Please enter a number.")
            continue

        behaviour_index = int(behaviour_choice) - 1

        if behaviour_index < 0 or behaviour_index >= len(behaviours):
            print("Behaviour number not found.")
            continue

        behaviour = behaviours[behaviour_index]
        log.add_behaviour(behaviour)
        week_1.refresh()
        save_app_data()
        print(f"Added {behaviour.name} ({behaviour.points:+}) to {log.date}.")
        print(f"New daily score: {log.daily_score:+}")
        print(f"New weekly score: {week_1.weekly_score}")


def add_note_to_day():
    log = choose_day()

    if log is None:
        return

    note = input("Enter note: ")
    log.add_note(note)
    save_app_data()
    print("Note added.")


def create_custom_behaviour():
    name = input("Behaviour name: ")
    category = input("Category: ")

    print("\nBehaviour type:")
    print("1. Bonus")
    print("2. Deduction")
    reward_type_choice = input("Enter your choice: ")

    if reward_type_choice == "1":
        reward_type = "Bonus"
    elif reward_type_choice == "2":
        reward_type = "Deduction"
    else:
        print("Invalid behaviour type.")
        return

    points_text = input("Points: ")

    if not points_text.isdigit():
        print("Please enter a whole number for points.")
        return

    points = int(points_text)

    if reward_type == "Deduction":
        points = -points

    behaviour = Behaviour(name, category, reward_type, points)
    behaviour.custom = True
    added = behaviour_catalogue.add_behaviour(behaviour)

    if added:
        save_app_data()
        print(f"Added new behaviour: {behaviour.name} ({behaviour.points:+})")


def view_past_weeks():
    data = load_data()
    saved_account = get_current_account_data(data)

    if saved_account is None:
        print("No saved account found.")
        return

    past_weeks = saved_account.get("past_weeks", [])

    if len(past_weeks) == 0:
        print("No past weeks yet.")
        return

    print("\n===== Past Weeks =====")

    for index, past_week in enumerate(past_weeks, start=1):
        print(f"{index}. {past_week['week_start']} to {past_week['week_end']} - {past_week['weekly_score']} XP - {past_week['reward']}")

    week_choice = input("Choose a week number to view, or 0 to go back: ")

    if week_choice == "0":
        return

    if not week_choice.isdigit():
        print("Please enter a number.")
        return

    week_index = int(week_choice) - 1

    if week_index < 0 or week_index >= len(past_weeks):
        print("Week not found.")
        return

    past_week = past_weeks[week_index]
    print("\n===== Past Weekly Summary =====")
    print(f"Week: {past_week['week_start']} to {past_week['week_end']}")
    print(f"Weekly XP: {past_week['weekly_score']}")
    print(f"Reward: {past_week['reward']}")
    print("\nDaily Scores:")

    for day_name, log in past_week["daily_logs"].items():
        print(f"{day_name.title()} ({log['date']}): {log['score']:+}")

        for behaviour_name in log["behaviours"]:
            print(f"  - {behaviour_name}")

        if log["notes"]:
            print(f"  Notes: {log['notes']}")


while True:
    print("\n===== RiseUp Kids Menu =====")
    print("1. Record Behaviour")
    print("2. View Daily Log")
    print("3. Add Note to Day")
    print("4. View Weekly Summary")
    print("5. Check Reward Unlocked")
    print("6. View Progress Graph")
    print("7. View Rewards")
    print("8. View Behaviour Catalogue")
    print("9. Add Your Own Behaviour")
    print("10. View Past Weeks")
    print("11. Export History")
    print("12. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_behaviour_to_day()
    elif choice == "2":
        log = choose_day()

        if log:
            log.show_summary()
    elif choice == "3":
        add_note_to_day()
    elif choice == "4":
        week_1.refresh()
        week_1.show_summary()
    elif choice == "5":
        week_1.refresh()
        reward_manager.unlock_reward(child_1, week_1.weekly_score)
    elif choice == "6":
        week_1.refresh()
        week_1.show_progress_graph()
    elif choice == "7":
        reward_manager.show_rewards()
    elif choice == "8":
        behaviour_catalogue.show_behaviour_list()
        print("\n1. List Bonus Behaviours")
        print("2. List Deduction Behaviours")
        sub_choice = input("Enter your choice: ")
        if sub_choice == "1":
            behaviour_catalogue.list_bonus_behaviours()
        elif sub_choice == "2":
            behaviour_catalogue.list_deduction_behaviours()
    elif choice == "9":
        create_custom_behaviour()
    elif choice == "10":
        view_past_weeks()
    elif choice == "11":
        week_1.refresh()
        week_1.export_history("riseup_history.csv")
    elif choice == "12":
        save_app_data()
        print("Exiting RiseUp Kids. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
