# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
x = input('Ixtiyoriy ikkata son kiriting: ')
y = input('Yana son kiriting: ')
if x == y :
  son = 'Sonlar o`zaro teng.'
elif x > y :
  son = f'{x} soni {y} dan katta son.'
elif x < y:
  son = f'{x} soni {y} dan kichik son'
print(son)