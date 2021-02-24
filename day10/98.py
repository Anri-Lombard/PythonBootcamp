def is_leap(chosen_year):
    """Takes the chosen year and returns True for a leap year
    and false for a normal year"""
    if chosen_year % 4 == 0:
        if chosen_year % 100 == 0:
            if chosen_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(chosen_year, chosen_month):
    """Takes the chosen year and month and returns the number
    of days in that month for either a leap or normal year"""
    if chosen_month > 12 or chosen_month < 1:
        return "There is no such month."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_or_not = is_leap(chosen_year)
    if leap_or_not:
        month_days[1] += 1
    real_month = chosen_month - 1
    return month_days[real_month]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

