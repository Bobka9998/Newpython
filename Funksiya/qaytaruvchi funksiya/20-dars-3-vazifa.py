###   Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

# def aylana_info(r):
#   """Aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
#   s = (r**2)*3.14
#   d = 2*r
#   l = 3.14*d
#   aylana = {
#     'raduis':r,
#     'diametr':d,
#     'uzunlik':l,
#     'yuzi':s
#   }
#   aylana['raduis']=r
#   aylana['diametr']=d
#   aylana['uzunlik']=l
#   aylana['yuzi']=s

#   print(aylana)
#   return aylana

# aylana_info(985)


### boshqacha yechimda natija bir xil

def aylana_info(radius,pi=3.14):
    aylana = {"radius":radius,
              "diametr":2*radius,
              "perimetr":2*radius*pi,
              "yuza":pi*radius**2
              }
    print(aylana)
    return aylana

aylana_info(12548700)