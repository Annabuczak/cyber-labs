import datetime  # this option keep track of the current date
import json  # built-in library saves and loads data from a file

total_words = 0

today_date = datetime.date.today()
print(today_date)

transactions = []  # stores all transactions while the program is running


def get_valid_date():  # asks the user for a valid date
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d")  # check format
            return date_input  # return valid date
        except ValueError:
            print("That date format isn’t right, try again.")


def load_data():  # loads saved transactions if the file exists, otherwise starts empty
    global transactions
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []  # start empty if file not found


load_data()  # load previous transactions at the start


def enter_date():  # checks the date format is correct
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Please enter the date in the correct format.")


def reset_all_data():  # clears all saved transactions
    global transactions
    confirm = input("Delete all data? (y/n): ")

    if confirm.lower() == "y":
        transactions = []
        save_data()
        print("All data cleared.")
    else:
        print("Cancelled.")


def delete_transaction():  # deletes a chosen transaction
    if not transactions:
        print("You haven’t added anything yet")
        return

    print("\n-- Your transactions --")
    for i, t in enumerate(transactions):
        print(f"{i}: {t['category']} | £{t['amount']:.2f} | {t['date']}")

    try:
        index = int(input("Which number do you want to remove? "))
        removed = transactions.pop(index)
        save_data()
        print(f"Removed £{removed['amount']:.2f} from {removed['category']}")
    except (ValueError, IndexError):
        print("That number isn’t valid.")


def menu():  # displays all available options
    print("\n--Financial Transactions --")
    print("1. Record income")
    print("2. Record expense")
    print("3. View reports")
    print("4. Show balance")
    print("5. Data options")
    print("6. Clear all data")
    print("7. Leave program")


def add_transactions(t_type, t_amount, t_date, t_category, t_note):  # adds a new transaction to the list
    transactions.append({
        "type": t_type,
        "amount": t_amount,
        "date": t_date,
        "category": t_category,
        "note": t_note if t_note.strip() else "None",  # use "None" if no note is given
    })
    save_data()
    print(f"Transaction added: £{t_amount:.2f} for {t_category} ({t_date})")


def show_balance():  # calculates and shows the balance
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expense
    if balance > 0:  # show status
        print("You are in profit.")
    elif balance < 0:
        print("You are spending more than you earn.")
    else:
        print("Your balance is even.")

    print("\n--- Balance ---")
    print(f"Income : £{income:.2f}")
    print(f"Expense: £{expense:.2f}")
    print(f"Total  : £{balance:.2f}")


def monthly_summary():  # shows totals for the current month
    if len(transactions) == 0:
        print("You haven’t added any transactions.")
        return

    current_month_prefix = datetime.date.today().strftime("%Y-%m")  # get current month
    total_income = 0.0
    total_expense = 0.0

    for t in transactions:
        if str(t["date"]).startswith(current_month_prefix):  # filter by month
            if t["type"] == "income":
                total_income += t["amount"]
            elif t["type"] == "expense":
                total_expense += t["amount"]

    net_balance = total_income - total_expense

    print("\n--- This Month ---")
    print(f"Money in : £{total_income:.2f}")
    print(f"Money out: £{total_expense:.2f}")
    print(f"Balance  : £{net_balance:.2f}")


def category_summary():  # shows totals for each category
    if len(transactions) == 0:
        print("You haven’t added anything yet.")
        return

    income_totals = {}
    expense_totals = {}

    for t in transactions:  # go through each transaction
        cat = t["category"]
        amount = t["amount"]

        if t["type"] == "income":  # add amount to the correct income category
            income_totals[cat] = income_totals.get(cat, 0) + amount
        elif t["type"] == "expense":
            expense_totals[cat] = expense_totals.get(cat, 0) + amount

    print("\n--- Income ---")
    if not income_totals:
        print("No income to show.")
    else:
        for cat, total in income_totals.items():
            print(f"  {cat}: £{total:.2f}")

    print("\nExpense by category:")
    if not expense_totals:
        print("No spending yet.")
    else:
        for cat, total in expense_totals.items():
            print(f"  - {cat}: £{total:.2f}")


def highest_lowest_expense():  # shows which category has the most and least spending
    expense_totals = {}

    for t in transactions:
        if t["type"] == "expense":
            cat = t["category"]
            expense_totals[cat] = expense_totals.get(cat, 0) + t["amount"]

    if not expense_totals:
        print("No spending data yet.")
        return

    highest = max(expense_totals, key=expense_totals.get)
    lowest = min(expense_totals, key=expense_totals.get)

    print(f"\nYou spent the most on {highest}: £{expense_totals[highest]:.2f}")
    print(f"You spent the least on {lowest}: £{expense_totals[lowest]:.2f}")


def search_transactions():  # lets the user search through transactions
    if len(transactions) == 0:
        print("Nothing to search yet.")
        return

    print("\n--- Find Transactions ---")
    target_month = input("Month (YYYY-MM) or press Enter to skip: ").strip()
    target_category = input("Category or press Enter to skip: ").strip()

    print("\n-- Search Results --")
    found_any = False

    for t in transactions:
        match_month = (target_month == "") or str(t["date"]).startswith(target_month)
        match_category = (target_category == "") or (t["category"].lower() == target_category.lower())

        if match_month and match_category:
            print(f"{t['date']} | {t['type'].capitalize()} | {t['category']} | £{t['amount']:.2f} | {t['note']}")
            found_any = True

    if not found_any:
        print("No matching transactions found.")


def save_data():  # saves data to a file
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)


while True:
    menu()

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            print("\n--- Add Income ---")
            print("1. Salary")
            print("2. Freelance work")
            print("3. Other income")
            print("4. Back to main menu")

            income_choice = input("Choose an option: ")

            if income_choice == "4":
                print("Back to main menu.")
                break

            if income_choice == "1":
                category = "Salary"
            elif income_choice == "2":
                category = "Freelance work"
            elif income_choice == "3":
                category = "Other income"
            else:
                print("That option isn’t valid, try again.")
                continue

            while True:
                try:
                    amount = float(input("Add the amount: "))
                    break
                except ValueError:
                    print("Please add a number only.")

            date_choice = input(
                "Use today’s date? (y/n): ").strip().lower()  # use manual date if user doesn’t choose today
            if date_choice == "y":
                date = datetime.date.today().strftime("%Y-%m-%d")
            else:
                date = enter_date()

            note = input("Add a note (optional): ")

            add_transactions("income", amount, date, category, note)

    elif choice == "2":
        while True:
            print("\n--- Record expense ---")
            print("1. Bills")
            print("2. Groceries")
            print("3. Transport")
            print("4. Entertainment")
            print("5. Other spending")
            print("6. Back to main menu")

            expense_choice = input("Choose an option: ")

            if expense_choice == "6":
                print("Back to main menu.")
                break

            if expense_choice == "1":
                category = "Bills"
            elif expense_choice == "2":
                category = "Groceries"
            elif expense_choice == "3":
                category = "Transport"
            elif expense_choice == "4":
                category = "Entertainment"
            elif expense_choice == "5":
                category = "Other spending"
            else:
                print("That option isn’t valid, try again.")
                continue

            while True:
                try:
                    amount = float(input("Add the amount: "))
                    break
                except ValueError:
                    print("Please enter a number only.")

            date_choice = input("Use today’s date? (y/n): ").strip().lower()
            if date_choice == "y":
                date = datetime.date.today().strftime("%Y-%m-%d")
            else:
                date = get_valid_date()

            note = input("Add a note (optional): ")

            add_transactions("expense", amount, date, category, note)

    elif choice == "3":
        while True:
            print("1. Monthly overview")
            print("2. Show total income")
            print("3. Show total spending")
            print("4. Show balance")
            print("5. View categories")
            print("6. Highest and lowest spending")
            print("7. Back to main menu")

            reports_choice = input("Choose an option: ")

            if reports_choice == "7":
                print("Back to main menu.")
                break
            elif reports_choice == "1":
                monthly_summary()
            elif reports_choice == "2":
                t_income = sum(t["amount"] for t in transactions if t["type"] == "income")
                print(f"\nIncome total: £{t_income:.2f}")
            elif reports_choice == "3":
                t_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
                print(f"\nTotal spent: £{t_expense:.2f}")
            elif reports_choice == "4":
                show_balance()
            elif reports_choice == "5":
                category_summary()
            elif reports_choice == "6":
                highest_lowest_expense()
            else:
                print("That isn’t one of the available options.")

    elif choice == "4":
        show_balance()

    elif choice == "5":
        while True:
            print("\n--- Data ---")
            print("1. Search transactions")
            print("2. Delete a transaction")
            print("3. Back to main menu")

            data_choice = input("Choose an option: ")
            if data_choice == "1":
                search_transactions()
            elif data_choice == "2":
                delete_transaction()
            elif data_choice == "3":
                break
            else:
                print("That option isn’t valid.")

    elif choice == "6":
        reset_all_data()
    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("That option isn’t valid, try again.")
