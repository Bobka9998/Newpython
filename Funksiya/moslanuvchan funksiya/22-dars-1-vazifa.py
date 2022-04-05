#   Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def kopaytma(*sonlar):
  """Sonlarning ko`paytmasini hisoblaydigan funksiya"""

  d = 1
  for son in sonlar:
    d = d*son

  return d

print(kopaytma(1,2,3,4,5,6,7))