### Foydalanuvchidan x va y sonlarini olib, 'x'ning 'y'chi darajasini konsolga chiqaruvchi funksiya yozing.
def daraja_count(x,y):
  """ x ning y chi darajasini hisoblash funksiyasi"""
  print(f'{x**y}.')

x = float(input('x soni uchun qiymat kiriting: '))
y = float(input('x soning darajasi uchun, y qiymat kiriting. '))
daraja_count(x,y)