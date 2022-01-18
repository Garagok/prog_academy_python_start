number = int(input('Type your number: '))

reverse = 0    # Reverse function

while number > 0:
    remain = number % 10    # Remain of our number
    reverse = (reverse * 10) + remain
    number //= 10   # # To keep the number intact

print(reverse)
