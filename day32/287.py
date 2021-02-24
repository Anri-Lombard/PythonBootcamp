import smtplib

my_email = "anrihappybirthday@yahoo.com"
my_password = "nqaebyjxhvvusyqq"

connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="anri.m.lombard@gmail.com",
    msg="Subject:Happy Birthday!\n\nI love you Anri! Have an awesome day!"
)
connection.close()
