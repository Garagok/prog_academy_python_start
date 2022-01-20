# Write a Python program to print the number entered by user only if the number entered is negative.
num = int(input('Enter a negative number: '))

print(num) if num < 0 else print('Entered number is NOT negative')
