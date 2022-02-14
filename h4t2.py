palindrome = int(input('Enter a six-digit number: '))

p1 = palindrome // 100000
p2 = palindrome % 100000 // 10000
p3 = palindrome % 10000 // 1000
p4 = palindrome % 1000 // 100
p5 = palindrome % 100 // 10
p6 = palindrome % 10 // 1

if (p1 + p2 + p3) == (p4 + p5 + p6):
    print('It is a palindrome')
else:
    print('It is not a palindrome')
