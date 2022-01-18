number = input('Type your number: ')
string1 = str(number)    # Transforming our number into string

summa = 0   # Sum for elements of our number

for element in string1:
    summa += int(element)    # Summing every element of our number; Transforming our number into int

print(summa)
