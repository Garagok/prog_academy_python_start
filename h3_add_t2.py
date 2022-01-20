# Leap year task
year = int(input('Enter the year: '))

# Leap year conditions check
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print('This is a leap year')
# Conditions failed
else:
    print('This is a default year')
