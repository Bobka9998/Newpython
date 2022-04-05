### Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

def bolinish_alomatlari(son):
    """kiritilgan soning 2 dan 10 gacha qoldiqsiz bo`linadigan sonlarni ekranga chiqarish funksiyasi"""
    for n in range(2,11):
      if son%n==0:
        print(f'{son}, {n} ga qoldiqsiz bo`linadi.')
      else:
        print(f'{son} {n} ga qoldiqsiz bo`linmaydi.')

son = int(input('Butun son kiriting: '))
bolinish_alomatlari(son)