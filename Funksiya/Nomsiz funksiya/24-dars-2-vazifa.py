### ikki son qabul qilib, ularning yig'indisini qaytaruvchi lambda funksiya yarating


while True:
  s = float(input('x ga qiymat kiriting: '))
  d = float(input('y ga qiymat kiriting: '))
  yigindi = lambda x,y:x+y
  print(yigindi(s,d))
  savol = input('Yana son kiritasizmi (yes/no): ')
  if savol=='no':
    print('Rahmat!!!')
    break
