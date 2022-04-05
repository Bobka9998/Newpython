# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
buyurtmalar = []
while True:
 buyurtma = input(f'Hurmatli mijoz buyurtmagizni ayting>>> ')
 buyurtmalar.append(buyurtma)
 t = input(f'Yana buyurtma aytasizmi (ha/yo`q)>> ')
 if t != 'ha':
   break

print(f'Sizning buyurtmangiz.')
for m in buyurtmalar:
  print(m)
print(buyurtmalar)