import datetime as dt
from random import *
import smtplib

my_email = "anrihappybirthday@yahoo.com"
my_password = "nqaebyjxhvvusyqq"

if dt.datetime.now().weekday() == 2:
    with open("quotes.txt") as motivational_quotes:
        quote_list = motivational_quotes.readlines()
        print(f"{choice(quote_list)}")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="anri.m.lombard@gmail.com",
        msg=f"Subject:This is you monday quote!\n\n{choice(quote_list)}"
    )
    connection.close()

