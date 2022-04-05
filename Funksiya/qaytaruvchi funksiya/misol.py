##### Qaytaruvchi funnksiya

# def toliq_ism_yasa(ism, familya):
#    """Toliq ism qayturuvchi funksiya"""
#    toliq_ism = f'{ism} {familya}'
#    return toliq_ism


# talaba1 = toliq_ism_yasa('hasan', 'yusufov')
# talaba2 = toliq_ism_yasa('bobur', 'sultanov')
# print(f'{talaba1} va {talaba2} bugun darsga kelishdi.')

###### Ixtiyoriy argumetlar.

# def toliq_ism_yasa(ism, familya, ota_ismi=" "):
#    """To`liq ism qaytaeuvchi funksiya"""
#    if ota_ismi:
#       toliq_ism = f'{ism} {familya} {ota_ismi}'
#    else:
#       toliq_ism = f'{ism} {familya}'
#    return toliq_ism.title()

# talaba = toliq_ism_yasa("hasan", "yusufov")
# talaba1 = toliq_ism_yasa("ali",'alisherov','eshmatov')
# print(talaba,talaba1)


#####  FUNKSIYADAN LUG'AT QAYTARAMIZ.

# def avto_info(make, model, color, korobka, year, price=None):
#    """ Lug`at qaytaruvchi funksiya avtomobilar uchun. """
#    avto = {
#             'komponiya':make,
#             'model':model,
#             "color":color,
#             "korobka":korobka,
#             "year":year,
#             "price":price
#          }
#    return avto

# avto1 = avto_info("GM",'gentra','yashil','avtomat',2021, 15000)
# avto2 = avto_info('lada','xray','qora','avtomat',2022)
# avtomobilar = [avto1,avto2]
# for avtov in avtomobilar:
#    if avtov['price']:
#       price = avtov['price']
#    else:
#       price = 'Noma`lum'
#    print(f"{avtov['color']} {avtov['model']}. Narxi: {price}")


##### FUNKSIYADAN RO'YXAT QAYTARAMIZ


# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(2,15))

def oraliq1(min,max, qadam=None):
   sonlar= []
   while min<max:
      sonlar.append(min)
      if qadam:
         min += qadam
      else:
         min += 1
   return sonlar
print(oraliq1(1,25))
print(oraliq1(1,100,5))


######   FUNKSIYALARNI TSIKLDA ISHLATISH


def avto_info(make, model, rangi, korobka, year, price=None):
   """ Lug`at qaytaruvchi funksiya avtomobilar uchun. """
   avto = {
            'komponiya':make,
            'model':model,
            "rangi":rangi,
            "korobka":korobka,
            "year":year,
            "price":price
         }
   return avto


print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting.")
    make=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    price=input("Narhi: ")


    avtolar.append(avto_info(make, model, rangi, korobka, yili, price))

    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break

print('Salonimzdagi avtomobillar.')
for avto  in avtolar:
    if avto['price']:
        price = avto['price']
    else:
        price = "No`malum"
    print(f'{avto["rangi"].title()} {avto["model"].title()}, {avto["korobka"]} korbka. Narxi:{avto["price"]}.')

print(avtolar)