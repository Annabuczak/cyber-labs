# RiseUp Kids app
print("Welcome to RiseUp Kids")


class Child:
    def __init__(self, name,age):
        self.name = name
        self.age = age


child_name_1 = "Louie"
child_age_1 = 10
child_name_2 = "Dotty"
child_age_2 = 10

child_1 = Child(child_name_1,child_age_1)
child_2 = Child(child_name_2,child_age_2)

print(f"Hello, {child_1.name}'s parent!")
print(f"{child_1.name} is {child_1.age} years old")
print(f"{child_2.name} is {child_2.age} years old")




