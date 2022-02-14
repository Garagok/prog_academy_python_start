import random

payment = []

for i in range(12):
    payment.append(random.randint(7500, 15000))
print(payment)

av_payment = sum(payment) / 12

print(av_payment)
