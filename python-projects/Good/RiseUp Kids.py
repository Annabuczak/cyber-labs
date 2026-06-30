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



class Behaviour:
    def __init__(self, behaviour_name,category,type,points, ):
        self.behaviour = behaviour_name
        self.category = category
        self.type = type
        self.points = points

category = ["Responsibility", "Kindness", "Self-control","Honestly","Respect"]
type = ["Bonus", "Deduction"]
points = [1,2,3,4,5, -1,-2,-3,-4,-5]
behaviour_name =["Bed made","Bedroom tidy","Buddy walked",
"Helped Mum without asking",
"Accepted “No” first time",
"Good sportsmanship",
"Honest about mistake",
"Apologised sincerely",
"Included another child",
"Controlled frustration",
"Bed not made",
"Bedroom messy","Clothes on bathroom floor",
"Shoes left in hallway",
"Plate left upstairs",
"Didn’t clean after eating",
"Didn’t walk Buddy when asked",
"Didn’t complete chore",
"Talking back",
"Swearing",
"Slamming door"
"Ignored instruction",
"Asked again after 'No'",
"Begged for YouTube",
"Begged for phone",
"Begged for computer",
"Asked for Tesco money after refusing chores",
"Poor sportsmanship",
"Threatened another child",
"Deliberately rude",
"Took frustration out on Buddy",
"Refused to apologise"]