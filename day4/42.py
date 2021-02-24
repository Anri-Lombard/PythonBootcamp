import random

nameString = input("Enter everyone's names who shared the meal seperated by a comma:\n")
names = nameString.split(", ")

numberOfPeople = len(names)
pick = names[random.randint(0, numberOfPeople - 1)]
print(f"{pick} will pay for the meal today.")

