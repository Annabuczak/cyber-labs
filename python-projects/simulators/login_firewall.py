class LoginFirewall:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.failed_attempts = 0
        self.locked = False

    def login(self, username, password):
        print(f"username: {username}, password: {password}")

        if self.locked:
            print("Account is locked")
            return

        if username == self.username and password == self.password:
            print("Login successful")
            self.failed_attempts = 0
        else:
            self.failed_attempts += 1
            print("Login failed")
            print(f"failed attempts {self.failed_attempts}")

            if self.failed_attempts >= 3:
                self.locked = True
                print("Account locked")

    def reset(self):
        self.failed_attempts = 0
        self.locked = False
        print("Account reset")
        print(f"failed attempts {self.failed_attempts}")

    def status(self):
        if self.locked:
            print("Account is locked")
        else:
            print("Account is unlocked")

        print(f"Failed attempts: {self.failed_attempts}")


account_user1 = LoginFirewall("Anna", "password123")
account_user2 = LoginFirewall("John", "password456")
account_user3 = LoginFirewall("Louie", "password789")

account_user1.login("Anna", "wrong")
account_user1.login("Anna", "wrong")
account_user1.login("Anna", "wrong")
account_user1.login("Anna", "password123")

account_user1.status()

account_user1.reset()

account_user1.login("Anna", "password123")
account_user1.status()
