arr = []
nom = 0
sum = 0

for i in range(4):
    row = []
    for j in range(4):
        nom = nom+1
        row.append(nom)
        sum = sum+nom
    arr.append(row)
for k in arr:
    print(k)

print('Matrix sum: ', sum)
