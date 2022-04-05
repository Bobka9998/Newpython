### Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kv_kb_count(number):
  """kvadrati va kubni hisoblash funksiyasi"""
  print(f'{number} ning kvadrati: {number**2}.\n'
        f'{number} ning kubi: {number**3}.')

number = float(input('Son kiriting: '))
kv_kb_count(number)