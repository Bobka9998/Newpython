ismlar = ['jasur', 'ulug`', 'otojon', 'donyor']
print('Salom', ismlar[0].title())
print('Qalaysan', ismlar[1].title())
print('Bugun ko`rishamiz', ismlar[2].title())
sonlar = [1, -57, 68, 35.4, 201]
print(sonlar[1]+sonlar[0])
print(sonlar[1]*sonlar[4])
narxlar = [25000, 54000, 74000, 32000, 41000, 19000, 45000]
narxlar.append(78000)
narxlar.insert(1, 'kiyim')
del narxlar[4]
narxlar.remove(74000)
print(narxlar)
t_shaxslar = ['torres', 'david villa', 'gerrad', 'benayum', 'alonso']
z_shaxslar = ['salax', 'mane', 'jota', 'firmino', 'gomez', 'alkantara']
print('Men tarixiy futbolchilardan ', t_shaxslar[0].title(), ' bilan,')
print('Zamonaviy fulbolchilardan ', z_shaxslar[3].title(), ' bilan\nfutbol o`ynashni xohlardim.')
# Mehmonga chaqirmoqchi bo`lgan shaxslar
friends = []
friends.append('jasur')
friends.append('otjon')
friends.append('nodir')
friends.append('umid')
friends.append('xasan')
friends.append('begi')
print(friends)
print('Mehmonga keladigan do`stlarim:\n', str(friends))
friends.remove('nodir')
friends.append('shox')
friends.insert(0, 'sher')
friends.insert(3, 'umid aka')
print(friends)
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
mehmonlar = str(mehmonlar)
print('Mehmonga kelgaan do`stlarim:\n', mehmonlar.title())