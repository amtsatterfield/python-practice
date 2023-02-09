import datetime
from dateutil.relativedelta import relativedelta

NAME = input('Enter your name: ')
AGE = input('Enter your age: ')

def calculate_hundred(in_age):
    today = datetime.date.today()
    years = 100 - int(in_age)
    return today + relativedelta(years=years)

years_til_hundred = calculate_hundred(AGE)
print(f'Hi {NAME}, you will be 100 years old in {years_til_hundred.year}')