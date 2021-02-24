# Multiple if statements - DOES ALL CONDITIONS
print("Welcome to the rolercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rolercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("You need to pay $5.")
    elif age <= 18:
        bill = 7
        print("You need to pay $7.")
    else:
        bill = 12
        print("You need to pay $12.")

    wants_photo = input("Do you want a photo taken for S3 more? Y or N? ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("You need to grow before you could ride.")