### lambda >> Nomsiz funksiya


# Pythonning o'ziga xos xususiyatlaridan biri, nomsiz vaqtinchalik funksiyalar yaratish imkoniyati. Bunday funksiyalarni yaratishda def operatori o'rniga lambda operatori ishlatilgani uchun ham lambda funskiyalar deb ataladi.

# Nomsiz funksiya quydagicha yaratiladi>>> "lambda argument:ifoda"


# 1 - usul
import math
import numbers
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))
# 2 - usul
from math import pi
uzunlik = lambda pi , r : 2*pi*r
print(uzunlik(pi,10))

# x - ning y chi darajasini aniqlash lambda funksiyasi
product = lambda x,y: x**y
print(product(4,5))

def daraja(n):
  return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(kvadrat(5))
print(kub(2))

# Lambda funksiyalaridan argument sifatida boshqa funksyani qabul qiluvchi funksiyalar bilan ishlashda ham keng foydalaniladi. Misol uchun map() va filter() funksiyalari.

# map() Funksiya

# Bu funksiya argument sifatida ro'yxat (yoki lug'at) va boshqa bir funksiyani qabul qilib, ro'yxat elementlariga qabul qilingan funksya yordamida ishlov beradi. Tushunarli bo'lish uchun quyidagi misolni ko'ramiz.

from math import sqrt
sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)

number = list(range(11))
def daraja2(x):
  '''berilgan sonning kvadratini qaytaruvchi funksiya'''
  return x*x

print(list(map(daraja2,number)))

# Tepadagi funksiyani Lambda yoradamida yozamiz

sonlar = list(range(11))
kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)

# map() funksiyasi bir nechta ro'yxatlar ham uzatish mumkin :

a = [1,2,3,8,5]
b = [4,6,7,9,10]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

ismlar = ['ali','abdu','hasan', 'abdumalik']
print(list(map(lambda harf:harf.upper(),ismlar)))


#### filter()  Funksiyasi


# Bu funksiya ham argument sifatida ro'yxat va boshqa funskiyani qabul qilib oladi va berilgan ro'yxat elementlarini berilgan funksiya yordamida saralaydi. Bunda argument sifatida uzatilgan funksiya mantiqiy qiymat qaytarishi kerak (True yoki False).


import random as r
sonlarr = r.sample(range(100),k=10)
def jutfmi(x):
  '''x juft bo'lsa True, aks holda False qaytaruvchu funksiya'''
  return x%2==0

juft_sonlar =list(filter(jutfmi,sonlarr))
print(sonlarr)
print(juft_sonlar)

# tepadagi dasturni lambda funksiyada yozamiz

import random as r
sonlarr = r.sample(range(100),k=10)
juft_sonlar = list(filter(lambda x:x%2==0,sonlarr))
print(sonlarr)
print(juft_sonlar)


#Keling endi filter() funksiyasi yordamida matnlarni saralashga ham misollar ko'raylik.


mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)

# tepadagi dasturda mevalar ro'yxatidan b harfiga boshlanuvchi mevalarni ajratib oladi. Bu yerda biz matnlarga tegishli bo'lgan .startswith() metodidan foydalandik. Bu metod, berilgan matn shu harfdan boshlanadimi yoki yo'q tekshiradi va True yoki False qiymat qaytaradi.


mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)

# Quyidagi dastur esa `mevalar` ro'yxatidan nomi 5 yoki undan kam harfdan iborat mevalarni saralab oladi.

mevalar = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(mevalar)
