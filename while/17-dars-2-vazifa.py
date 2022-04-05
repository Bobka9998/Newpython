# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).



# savol = 'Yoshingizni kiriting: '
# while True:
#     qiymat = int(input(savol))
#     if qiymat == 'exit' or qiymat == 'quit':
#       break
#     yosh = qiymat
#     if yosh < 7 :
#       print('Kirish 2000 so`m')
#     elif yosh < 18 :
#       print('Kirish 3000 so`m')
#     elif yosh < 65:
#       print('Kirish 10000 so`m')
#     else:
#       print('Kirish bepul')
# print('Rahmat')


while True:
  age = input("Yoshingizni kiriting: ")
  if age == 'exit' or age == 'quit':
    break
  age = int(age)
  if age < 7:
    print('2000 so`m')
  elif  7 <= age < 18:
    print('3000 so`m')
  elif 18 <= age < 65:
    print('10 000 so`m')
  else:
    print('Bepul.')
print('Rahmat')


# Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
