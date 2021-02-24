height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2
reading = f"Your BMI is {bmi}, and "
if bmi < 18.5:
    reading += "you are underweight."
elif bmi < 25:
    reading += "you are normal weight."
elif bmi < 30:
    reading += "you are overweight."
elif bmi < 35:
    reading += "you are obese."
else:
    reading += "you are clinically obese."

print(reading)

