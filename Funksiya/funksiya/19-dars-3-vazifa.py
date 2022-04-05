### Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juft_toq_son_count(number):
  """Sonning juft yoki toqligini hisoblash funksiyasi"""
  if number%2==0:
    print(f'{number} juft son.')
  else:
    print(f'{number} toq son.')

number = int(input('Butun son kiriting: '))
juft_toq_son_count(number)