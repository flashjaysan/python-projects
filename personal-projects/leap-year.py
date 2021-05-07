def is_leap(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


years = [1900, 1996, 2000, 2004, 2010, 2020, 2100]
for year in years:
    if is_leap(year):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} isn\'t a leap year.')
