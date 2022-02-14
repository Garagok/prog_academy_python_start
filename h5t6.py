import random

list1 = []
list2 = []

for i in range(4):
    list1.append(random.randint(1, 9))
list2 = list1 * 2

for i in range(len(list2)):
    if i >= 4:
        list2[i] = list2[i] * 2

print(list1)
print(list2)
