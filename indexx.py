# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if float(qiymat)<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


# son = 0
# while son<10:

#     if son%2 !=0:
#         continue
#     else:
#         print(son, end=" ")


# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# for ism in ismlar:
#     print(ism)
# print(ismlar)


# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
# for c , d in baholangan_talabalar.items():
#     print( c.title() ,d , 'oldi' )
# from sklearn.utils import shuffle

# d = list(range(11))
# y =  shuffle(d)
# print(d)
# print(y)



# import math
# y = math.ceil(4.1)
# print(y)

# from fractions import Fraction
# a = Fraction(1, 7)
# b = Fraction(1, 3)
# print(a + b)

# import random as r
# ismlar = ['murod', 'otojon', 'bobur', 'husniddin', 'isroil']
# print(ismlar)
# print(r.shuffle(['murod', 'otojon', 'bobur', 'husniddin', 'isroil']))

print(5/2,5%2,5//2)