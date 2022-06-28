#  Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

def katta_harf(matnlar):
  for h in range(len(matnlar)):
    matnlar[h]=matnlar[h].title()
  return matnlar
royxat = ['salom', ' xayr', 'moshin', 'kema']
katta_harf(royxat)
print(royxat)


#def katta_harf(matnlar):
#    for i in range(len(matnlar)):
#        matnlar[i]=matnlar[i].title()

#ismlar = ['ali', 'vali', 'hasan', 'husan']
#katta_harf(ismlar)
#print(ismlar)

# Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

# def katta_harf(matnlar):
 #   for h in range(len(matnlar)):
#     matnlar[h]=matnlar[h].title()

#   return matnlar

# royxat = ['salom', ' xayr', 'moshin', 'kema']
# f = katta_harf(royxat[:])
# print(royxat)
# print(f)


# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar[:])
# print(ismlar)
# print(yangi_ismlar)


print('salom')