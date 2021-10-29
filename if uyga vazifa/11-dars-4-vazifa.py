# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mahsulotlar =['sabzi', 'kartoshka', 'piyoz', 'olma', 'yog`', 'tuz', 'gugurt', 'banan', 'uzum', 'anor', 'un']
savat = []
print('Beshta oladigan mahsulotingizni kiriting:')
for n in range(5) :
  savat.append(input(f'Savatga {n+1}-mahsulot oling:  '))
for mahsulot in savat:
  if mahsulot.lower() in mahsulotlar:
    print(f'Bu {mahsulot.title()} mahsulot do`konimizda bor.')
  else:
    print(f'Bu {mahsulot.title()} Mahsulot do`konimizda yo`q.')