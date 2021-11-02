# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
davlatlar = {'uzbekiston':'toshkent', 'qozog`iston':'nur-sulton', 'tojikiston':'dushanbe', 'avganiston':'kobul', 'turkmaniston':'ashgabot', 'rossiya':'moskva', 'turkiya':'istambul','angliya':'london','ispaniya':'madrid', 'fransiya':'parij', 'yaponiya':'tokio','xitoy':'pekin'}
print('Davlatlar ro`yxati:')
for davlat in sorted(davlatlar.keys()):
  print(f'{davlat.title()}')
print('Poytaxtlar ro`yxati.')
for poytaxt in sorted(davlatlar.values()):
  print(poytaxt.title())