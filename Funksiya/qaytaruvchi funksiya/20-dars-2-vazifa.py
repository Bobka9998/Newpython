# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
def katta_son(x,y,z):
  """3 ta sondan kattasini qaytaruvchi funksiya"""
  if y<x>z:
    print(x)
  elif x<y>z:
    print(y)
  elif x<z>y:
    print(z)
  return katta_son

katta_son(15,25,8)
katta_son(36,32,15)
katta_son(26,45,98)

#### yana bir usuli
# def kattasi(x,y,z):
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max