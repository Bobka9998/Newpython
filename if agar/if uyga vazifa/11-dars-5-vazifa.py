# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
mahsulotlar =['sabzi', 'kartoshka', 'piyoz', 'olma', 'yog`', 'tuz', 'gugurt', 'banan', 'uzum', 'anor', 'un']
savat = []
print('Beshta mahsulot oling')
for n in range(5):
  savat.append(input(f'Savatga {n+1}-mahsulotni yozing: '))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
  if mahsulot.lower() in mahsulotlar:
    bor_mahsulotlar.append(mahsulot)
  else:
    mavjud_emas.append(mahsulot)
if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
