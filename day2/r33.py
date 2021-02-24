age = input("What is your current age? ")

years_left = 90 - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {years_left} years, {months_left} months, {weeks_left} weeks,"
      f" or {days_left} days left if you live to 90.")