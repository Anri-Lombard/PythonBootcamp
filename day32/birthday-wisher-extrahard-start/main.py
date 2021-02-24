##################### Extra Hard Starting Project ######################
import pandas
import random
import datetime as dt
import smtplib

NOW = dt.datetime.now()
days = []
their_email = []
my_email = "anrihappybirthday@gmail.com"
my_password = "HappyBirthday"

# 1. Update the birthdays.csv
bd = pandas.read_csv("birthdays.csv")
bd_dataframe = pandas.DataFrame(bd)
bd_data = pandas.DataFrame.to_dict(bd)
for i in range(0, len(bd_data['day'])):
    days.append(bd_data['day'][i])

# 2. Check if today matches a birthday in the birthdays.csv
for i in range(len(days)):
    if days[i] == NOW.day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        random_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_number}.txt") as letter:
            random_letter = letter.read()
        new_random_letter = random_letter.replace("[NAME]", bd_dataframe.loc[i, 'name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=bd_data['email'][i],
            msg=f"Subject:Happy Birthday!\n\n{new_random_letter}"
        )
        connection.close()
        print("done")
