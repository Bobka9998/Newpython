# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqarish
davlatlar = ['rossiya', 'tojikiston', 'uzbekiston', 'litviya', 'latviya', 'fransiya', 'turkiya', 'ispaniya', 'angliya']
print(davlatlar, '\n')
# Ro'yxatning uzunligini konsolga chiqarish
print('Royxat uzunli: ',len(davlatlar), 'ta\n')
# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqarish
print(sorted(davlatlar),'\n')
print('Asil ro`yxat buzilmagan xolda:\n',davlatlar , '\n')
# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqarish
print('Asl ro`yxatni o`zgartirmasdan teskari tahlash uslibi "sorted()" yordamida:\n',sorted(davlatlar, reverse=True))
# Asl ro'yxatni qaytadan konsolga chiqarish
print('Asl ro`yxatni konsolga chiqarish:\n',davlatlar,'\n')
# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqarish
davlatlar.reverse()
print(davlatlar,'\n')
# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqarish
davlatlar.sort()
print('"sort()" yordamida ro`yxatni alifbo bo`yicha chiqarish\n', davlatlar)
# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200,2))
print(sonlar)
# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
jami = sum(sonlar)
print(jami)
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
kichik = min(sonlar)
katta = max(sonlar)
print(katta - kichik , '\n')
# Ro'yxatdagi elementlar sonini hisoblang
print(len(sonlar))
#  Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[259:279])
# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh', 'gamburg', 'lavash', 'shashlik', 'somsa', 'manti', 'kavob']
# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
print(nonushta)
nonushta.remove('osh')
nonushta.remove('somsa')
nonushta.remove('manti')
nonushta.remove('lavash')
nonushta.append('tuxum')
nonushta.append('saryog`')
print(nonushta)
print(taomlar)
# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non'