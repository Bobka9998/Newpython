# # Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# # Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())
# # Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# ism = input("Ismingizni kiriting:\n")
# if ism.lower() == 'admin':
#     print(f"Xush kelibsiz {ism.capitalize()} foydalanuvchilar ro`yxatini ko`rasizmi?")
# else:
#     print('Xush kelibsiz foydalanuvchi', ism.capitalize())
# # Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# x = int(input('Istagan songizni kirirting:\n'))
# y = int(input('Yana bitta son kirirting:\n'))
# if x == y:
#     print(f"Kiritgan soningiz bir biriga teng\n{x} = {y}")
# else:
#     print('Sonlar teng emas')
# # Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# son = int(input('Istagan son kiriting:\n'))
# if son < 0:
#     print('Kiritgan soningiz "Manfiy son"')
# else:
#     print('Kiritgan soningiz "Musbat son"')
# # Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
# number = int(input('Istagan soningizni kirirting:\n'))
# if number > 0 :
#     print(f"Siz kiritgan sonning ildizi {number**(1/2)} ga teng.")
# else:
#     print(input('Musbat son kiriting.\n'))


def oraliq(min,max,qadam= 1):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar

sonlar = oraliq(4,13,3)
print(sonlar)