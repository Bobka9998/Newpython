import random as r

def son_top(x):
  sonlar = list(range(1,x))
  taxmin_son = r.choice(sonlar)
  print(f'Keling o`yin o`ynaymiz. Men 1 dan {x} gacha son o`yladim topa olasizmi.', end='')
  taxminlar = 0
  while True:
    taxminlar += 1
    taxmin = int(input('>>> '))
    if taxmin_son > taxmin:
     print(f'Siz o`ylagan son kichik kattaroq son kiriting.', end='')
    elif taxmin_son < taxmin:
      print(f'Siz o`ylagan son katta kichikroq son kiriting.', end = ' ')
    elif taxmin_son == taxmin:
      print(f'Siz {taxminlar} urunish bilan topdingiz topdingiz. Javob {taxmin}')
      break
  return taxminlar


# def son_top_kom(x):
