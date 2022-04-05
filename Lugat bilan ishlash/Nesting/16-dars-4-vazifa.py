# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.
davlatlar = {
  'uzbekiston':{
                  'maydoni':448978,
                  'poytaxt':'toshkent',
                  'pul_birligi':'so`m',
                  'aholisi':33_000_000
                },
  'turkmaniston':{
                  'maydoni':488100 ,
                  'poytaxt':'ashxobod',
                  'pul_birligi':'manat',
                  'aholisi':7_000_000
                },
  'turkiya':{
                  'maydoni':783562,
                  'poytaxt':'ankara',
                  'pul_birligi':'turk lirasi',
                  'aholisi':81_000_000
                },
  'yaponiya':{
                  'maydoni':377835,
                  'poytaxt':'tokio',
                  'pul_birligi':'yen',
                  'aholisi':127_417_244
                }

}
for davlat, info  in davlatlar.items():
  print(f"{davlat.title()}ning poytaxti {info['poytaxt'].title()}.")
  print(f"Maydoni: {info['maydoni']} kv.km.")
  print(f"Aholisi: {info['aholisi']} kishi.")
  print(f"Pul birligi: {info['pul_birligi'].title()}")
