### Berilgan son tub bo'lsa , True , aks xolda False qaytaruvchi funksiya yozing.

while True:
  def tubmi(x=int(input('son kiriting: '))):
      if x % 2 == 0 or x < 2:
          return False  # Son juft yoki 2 dan kichik bo'lsa
      if x == 2 or x == 3:
          return True  # Son 2 yoki 3 bo'lsa
      for i in range(3, x, 2):
          if x % i == 0:
              return False
      return True

  print(tubmi())
# filter() va yuqordagi funksiya yordamida 1 dan 10000 gacha oraliqdagi tub sonlar ro'yxatini tuzing.

# sonlar = list(range(1,1000))
# tub_sonlar = list(filter(lambda x:x%2!=0,sonlar))
# print(tub_sonlar)
