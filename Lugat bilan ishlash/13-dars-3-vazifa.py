# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
python_lugat = {'list':'ro`yxat', 'int':'butun son', 'float':'o`nlik son', 'str':'mantinli yozuv', 'if':'shartli operator', 'title':'ro`xatdagi matnni har bir so`zni 1-harfni katta bilan yozadi', 'lower':'har birni kichik harfda yozadi ', 'capitalize':'faqat 1-harfni katta bilan yozadi.', ' upper':'Barcha harflarni katta bilan yozadi.', 'print':'Chop etish.'}
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
user = input('Python terminlaridan birini kiriting: ').lower()
print(python_lugat.get(user,'Bunday so`z mavjud emas'))
# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
user = input('Python terminlaridan birini kiriting: ').lower()
if user in python_lugat:
  print(python_lugat[user].capitalize())
else:
   print("Bunday so'z mavjud emas")