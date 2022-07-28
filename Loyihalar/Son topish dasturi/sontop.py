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
      print(f'Siz {taxminlar} urunish bilan topdingiz . Javob {taxmin}')
      break
  return taxminlar


def son_top_kom(x):
  past  = 1
  yuqori = x
  while True:
    if past != yuqori:
      taxmin_son = r.randint(past,yuqori)
    else:
      past = yuqori
    javob = input(f'{taxmin_son} son to`g`rimi. Ha to`g`ri(ok), kattaroq (+), kichikroq (-)'.lower())
    if javob == '+':
      past = taxmin_son + 1
    elif javob == '-':
      yuqori = taxmin_son - 1
    elif javob == 'ok':
      break


print(son_top_kom(10))