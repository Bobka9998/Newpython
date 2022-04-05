#  Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def katta_kichik_count(x,y):
    """ sonlarning katta , kichik va tenglikini hisoblash funksiyasi"""
    if x>y:
      print(f'{x} , {y} dan katta.')
    elif x<y:
      print(f'{x} , {y} dan kichik.')
    else:
      print(f'{x} = {y} o`zaro teng son.')

x = int(input('x uchun son qiymat kiriting. '))
y = int(input('y uchun son qiymat kiriting. '))
katta_kichik_count(x,y)