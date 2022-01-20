# Write a Python program to find largest number among three numbers entered by user
num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
num_3 = int(input('Enter the third number: '))

# num_1 check:
if num_1 > num_2 and num_1 > num_3:
    print('Number 1 is bigger than Number 2 and Number 3')
# num_2 check:
elif num_2 > num_1 and num_2 > num_3:
    print('Number 2 is bigger than Number 1 and Number 3')
# num_3 check:
elif num_3 > num_1 and num_3 > num_2:
    print('Number 3 is bigger than Number 1 and Number 2')
# Equality check
# num_1 and num_2 are equal and num_3 is lesser
elif num_1 == num_2 and num_3 < num_1 and num_3 < num_2:
    print('Number 1 and Number 2 are equal to each other and bigger than Number 3')
# num_1 and num_3 are equal and num_2 is lesser
elif num_1 == num_3 and num_2 < num_1 and num_2 < num_3:
    print('Number 1 and Number 3 are equal to each other and bigger than Number 2')
# num_2 and num_3 are equal and num_1 is lesser
elif num_2 == num_3 and num_1 < num_2 and num_1 < num_3:
    print('Number 2 and Number 3 are equal to each other and bigger than Number 1')
# All numbers are equal
else:
    print('Given numbers are equal to each other')
