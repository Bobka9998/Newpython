# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
filmlar = {
  'ali':['kun', 'o`yin','g`alaba','ishonch'],
  'vali':['musobaqa','iroda','tenglik','kelgindi'],
  'usmon':['taqdir','hayot','saboq','kelushuv'],
  'patrik':['sevgi','azob','tuyg`u','erkinlik']
}
for ism, kinolar in filmlar.items():
  print(f"{ism.title()}ning sevimli kinolari wular:")
  for kino in kinolar:
    print(kino.title())