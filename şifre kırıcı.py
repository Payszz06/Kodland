import random

q = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

q_uzunluk = int(input("Kaç karakter olsun"))
q_adet = int(input("Kaç tane olsun"))
for y in range(0,q_adet):
    qn = ""
    for i in range(0, q_uzunluk):
        q2 = random.choice(q)
        qn = qn + q2
    print("Random sifreniz", qn)
