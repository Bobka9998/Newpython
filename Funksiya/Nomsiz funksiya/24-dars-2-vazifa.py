### ikki son qabul qilib, ularning yig'indisini qaytaruvchi lambda funksiya yarating


while True:
  yigindi = lambda x,y:x+y
  s = float(input('x ga qiymat kiriting: '))
  d = float(input('y ga qiymat kiriting: '))
  print(yigindi(s,d))
  savol = input('Yana son kiritasizmi (yes/no): ')
  if savol=='no':
    break
  else:
    continue

print('Rahmat!!!')