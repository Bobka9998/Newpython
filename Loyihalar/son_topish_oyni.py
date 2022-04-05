from ast import While
import random as r
def son_top(x):
  sonlar = list(range(1,x))
  son = r.choice(sonlar)
  #return son
  taxmin = int(input(f'1 dan {x} gacha son o`yladim. Topa olasizmi.\n>>> '))
  # while True:
  if son == taxmin:
    print('Javob to`g`ri.')
  elif son > taxmin:
    print(f'Javob, siz o`ylagan sondan kichik.')
  elif son < taxmin:
    print(f'Javob, siz o`ylagan sondan katta.')
print(son_top(10))