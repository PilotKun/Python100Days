age = input("what is your age? ")
# 365 days, 52 weeks, 12 months, expected to live till 90

age_as_int = int(age)
years_left = 90 - age_as_int
days_left = years_left*365
weeks_left = years_left*52
months_left = years_left*12

print(f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left.")