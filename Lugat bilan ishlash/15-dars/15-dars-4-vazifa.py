# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
menu = {
          'osh':12000,
          'somsa':7000,
          'norin':15000,
          'shashlik':7000,
          'gamburg':7000,
          'lag`mon':14000,
          'kavob':70000,
          'tuxum barak':12000,
          'manti':13000,
          'shorva':11000,
          'tuxum': 8000
        }
print('3 ta taom buyurtma qiling: ')
buyurtmalar = []
for b in range(3):
  buyurtmalar.append(input(f'{b+1}-taomni ayting: ').lower())

for buyurtma in buyurtmalar:
  if buyurtma in menu:
    print(f'{buyurtma.title()}ning  narxi {menu[buyurtma]}')
  else:
    print(f"Kechirasiz, bizda {buyurtma} yo'q.")
