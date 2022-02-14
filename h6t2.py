arr = []
kol = 0
n2 = 0
name = str(input("Enter some name: "))
print(name)

for i in name:
    if i.isalpha():
        arr.append(i)
        kol = kol + 1
    if i.isupper():
        n2 = n2 + 1
if kol == len(arr) and n2 == 1:
    print('Name is OK')
else:
    print('Name is invalid')

