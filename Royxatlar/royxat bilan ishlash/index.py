# // Ro`yxat bilan ishlash
# ro`yxatni alifbo ketma-ketlik bilan taxlashimiz uchun bizga : ".sort()" metodidan foydalanamiz.
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars, '\n')
# Diqqat! Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling. Agar matndagi so'zlarning bosh harfi katta-kichik aralash yozilgan bo'lsa, ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars, '\n')
# Ro'yxatni teskari tartibda saqlash uchun ".sort()" metodi ichida "reverse=True" argumentini ham kiritamiz. 
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars, '\n')
# ".sort()" metodi ro'yxatni tartiblaydi. Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini 
# buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun "sorted()" funktsiyasidan foydalanamiz:
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
# sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz:
print(sorted(mehmonlar, reverse=True))
print('Orginal: ', mehmonlar , '\n')
# Yuqordagi metod bilan sonlarga ham ishlatsa bo`ladi
# // Ro`yaxatni aylantirish
# Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) 
# talab qilinishi mumkin. Buning uchun .reverse() metodidan foydalanamiz.
fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits , '\n')
# //  RO'YXATNING UZUNLIGINI BILISH
# Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun "len()" funktsiyasidan foydalanamiz:
fruits = ['pear','banana','apple','watermelon','lemon']
print("Elementlar soni:",len(fruits), '\n') # len(fruits) ro'yxat uzunligini qaytaradi.
# range() FUNKTSIYASI 
# Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. 
# "list()" funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
narxlar = list(range(0,25))
print(narxlar, '\n')
# range() yordamida qadam ham berishimiz mumkin
sonlar = list(range(0,60,6))
print(sonlar, '\n')
# // SONLI RO'YXAT USTIDA SODDA AMALLAR
# Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin.
# Misol uchun ro'yxatdagi eng kichik sonni topish uchun "min()" funktsiyasidan, 
# eng katta sonni topish uchun esa "max()" funktsiyasidan, sonlarning yig'indisini 
# topish uchun esa "sum()" funktsyasidan foydalansak bo'ladi:
narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)