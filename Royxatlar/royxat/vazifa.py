# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['jasur', 'ulug`', 'otojon', 'donyor']
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
print('Salom', ismlar[0].title())
print('Qalaysan', ismlar[1].title())
print('Bugun ko`rishamiz', ismlar[2].title())
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [1, -57, 68, 35.4, 201]
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
print(sonlar[1]+sonlar[0])
print(sonlar[1]*sonlar[4])
sonlar[0] = 25
narxlar = [25000, 54000, 74000, 32000, 41000, 19000, 45000]
narxlar.append(78000)
narxlar.insert(1, 'kiyim')
del narxlar[5]
narxlar.remove(74000)
print(narxlar)
# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['torres', 'david villa', 'gerrad', 'benayum', 'alonso']
z_shaxslar = ['salax', 'mane', 'jota', 'firmino', 'gomez', 'alkantara']
print('Men tarixiy futbolchilardan ', t_shaxslar[0].title(), ' bilan,')
print('Zamonaviy fulbolchilardan ', z_shaxslar[3].title(), ' bilan\nfutbol o`ynashni xohlardim.')
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
t_futbolist = t_shaxslar.pop(0)
z_futbolist = z_shaxslar.pop(-1)
print(f'9-raqam egasi {t_futbolist.title()} va 10-raqam egasi {z_futbolist.title()} Liverpoolning kuchli futbolchilari hisoblanadi.')
# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append('jasur')
friends.append('otjon')
friends.append('nodir')
friends.append('umid')
friends.append('xasan')
friends.append('begi')
print(friends)
print('Mehmonga keladigan do`stlarim:\n', str(friends))
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove('nodir')
# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('shox')
friends.insert(0, 'sher')
friends.insert(3, 'umid aka')
print(friends)
# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
mehmonlar = str(mehmonlar)
print('Mehmonga kelgaan do`stlarim:\n', mehmonlar.title())