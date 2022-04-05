###   Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)


def tub_son(min,max):
  tub_sonlar = []
  for n in range(min,max):
      tub = True
      if n==1:
        tub = False
      elif n==2:
        tub = True
      else:
        for x in range(2,n):
          if (n%x==0):
            tub= False

      if tub:
        tub_sonlar.append(n)

  sonlar = []
  while min<max:
    sonlar.append(min)
    min += 1


  print(sonlar)
  print(tub_sonlar)
  return tub_sonlar


tub_son(1,33)