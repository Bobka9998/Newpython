# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
e_bozor = {}
r = True
while r :
  mahsulot = input(f'Mahsulot nomini kiriting?>> ')
  narx = float(input(f'{mahsulot.capitalize()}ning narxini kiriting?>> '))
  e_bozor[mahsulot] = narx

  javob = input(f'Yana mahsulot va narx kiritasizmi (ha/yo`q)>> ')
  if javob == "yo`q":
    r = False

print(f'Mahsulotlar va narxlar ro`yxati.')
for mahsulot , narx in e_bozor.items():
  print(f'{mahsulot.capitalize()}ning narxi {narx} so`m')
print(e_bozor)