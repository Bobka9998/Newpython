# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
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
davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
  info = davlatlar[davlat]
  print(f"\n{davlat.capitalize()}ning poytaxti: {info['poytaxt'].title()}"
          f"\nHududi: {info['maydoni']} kv.km teng."
          f"\nAholisi: {info['aholisi']}."
          f"\nPul birligi: {info['pul_birligi']}.")
else:
  print(f"Bizda {davlat.title()} haqida ma`lumot yo`q.")