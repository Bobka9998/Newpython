


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




def avto_kirit():
  """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
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
  return avtolar



def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rangi'].title()} {avto_info['komponiya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['year']}-yil, {avto_info['price']}$")
