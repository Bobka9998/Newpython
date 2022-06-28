# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil).

def mijoz_info(name, surname, year, place, email=None, number=None):
    """Lug`at qaytaruvchi funksiya mijozlar ma`lumoti """
    mijoz = {
        'ism':name,
        'familya':surname,
        't_yil':year,
        't_joy':place,
        'e_manzil':email,
        'tel_raqam':number
    }
    return mijoz

print("Ma`lumotlarindizni kiriting:")
mijozlar =[]
while True:
    name = input('Ismingizni kiriting: ')
    surname = input('Familyangizni kiriting: ')
    year = input('Tug`ulgan yilingzni kiriting: ')
    place = input('Tug`ulgan oyingizni kiriting: ')
    email = input('Elektron pochtangizni kiriting: ')
    number = input('Telefon raqamingizni kiriting: ')
    #Foydalanuvchi kiritdan ma'lumotlardan mijoz_info yordamida lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    mijozlar.append(mijoz_info(name, surname, year, place, email, number))

    savol = input("Yana ma`lumot kiritasizmi? (yes/no): ")
    if savol=='yes':
        continue
    elif savol=='no':
        break

print(f'Bizdagi ishchilarning ma`lumotlari.')
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familya'].title()} {mijoz['t_yil']}-yilda tug`ulgan. Raqami {mijoz['tel_raqam']}.")
print(mijozlar)