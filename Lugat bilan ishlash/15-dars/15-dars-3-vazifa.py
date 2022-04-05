# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
davlatlar = {
              'uzbekiston':'toshkent',
              'qozog`iston':'nur-sulton',
              'tojikiston':'dushanbe',
              'avganiston':'kobul',
              'turkmaniston':'ashgabot',
              'rossiya':'moskva',
              'turkiya':'istambul',
              'angliya':'london',
              'ispaniya':'madrid',
              'fransiya':'parij',
              'yaponiya':'tokio',
              'xitoy':'pekin'
            }
davlat = input('Davlat nomini kiriting: ').lower()
poytaxt = davlatlar.get(davlat)
if poytaxt== None:
  print('Bu davlat haqida ma`lumot yo`q bizda !')
else:
  print(f'{davlat.title()}ning poytaxti {poytaxt.title()}.')