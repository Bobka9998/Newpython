### Python modullari>> math Modullari.

# sqrt() >> qavs ichida berilgan qiymatni kvadrat ildizini qaytaradi

from math import sqrt # import math
a = 9
print(sqrt(a)) # print(math.sqrt(a))

import math
print(math.pow(5,4)) # pow(x,y)  x ning n chi darajasini hisoblaydi

print(math.pi) # pi -  ning qiymatini saqlovchi o'zgaruvchi

print(math.log2(8)) # logx(y) - logarifim hisoblaydi


### random MODULI >>> random moduli tasodifiy sonlar bilan ishlash uchun qulay funksiyalarga boy.

import random as r
son = r.randint(1,100)  # randint(a,b) funksiyasi a va b sonlar orasida tasodifiy bun son qaytaradi
print(son)

ismlar = ['ali','abu','abdu','hasan','bobur','donyor','jasur']
ism = r.choice(ismlar) # choice(x) berilgan argumentning ichidan  tasodifiy element qaytaruvchi funksiya
print(ism)

c = list(range(1,54,5))
print(c)
print(r.choice(c))

# f = list(range(20))
# print(f)
# r.shuffle(f)

from sklearn.utils import shuffle

d = list(range(11))
y =  shuffle(d) # shuffle(x) - x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya. Bunda x bir necha elementdan iborat (matn,ro'yxat) bo'lishi kerak
print(d)
print(y)

from random import sample
x = list(range(0,57))
y = sample(x,k=5) # samle(x,k)>> x ro'yxatdan 10 ta element ajratib olish. k o'zgarmas argument
print(x)
print(y)
