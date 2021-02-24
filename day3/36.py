# "Angela".count("a") = 1 (counts only lower case a)
# lower_case_name = "Angela".lower()
# lower_case_name.count("a") = 2
print("Welcome to Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

t = name1.lower().count("t") + name2.lower().count("t")
r = name1.lower().count("r") + name2.lower().count("r")
u = name1.lower().count("u") + name2.lower().count("u")
e = name1.lower().count("e") + name2.lower().count("e")
l = name1.lower().count("l") + name2.lower().count("l")
o = name1.lower().count("o") + name2.lower().count("o")
v = name1.lower().count("v") + name2.lower().count("v")

first_digit = t + r + u + e
second_digit = l + o + v + e

before_score = str(first_digit) + str(second_digit)
score = int(before_score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score < 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
