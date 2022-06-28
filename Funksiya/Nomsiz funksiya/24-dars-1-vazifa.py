## Berilgan sonni 10 ga ko`payturuvchi lambda funksiya

while True:
  print('Kiritgan soningizni 10  ko`paytirish funksiyasi')
  son = lambda son:son*10
  print(son(float(input('son kiriting: '))))
  savol = str(input('Yana hisoblaysizmi (yes)/(no): '))
  if savol == 'no':
    print('rahmat')
    break
