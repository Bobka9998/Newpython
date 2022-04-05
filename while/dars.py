# # while bilan amallar.
son = 1
while son<=5:
  print(son, end=' ')
  son = son +1

# # Kiritilgan sonning kvadratini qaytaruvchi dastur.
print("\nKiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print('Dastur tugadi!')
# #

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
        print('Dastur tugadi!')
    else:
        print(float(qiymat)**2)

# Break operatori.
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True: # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # tsiklni to'xtatish
    else:
        print(float(qiymat)**2)

# Break operatori for tsiklini to'xtatish uchun ham ishlatiladi.
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
        break
    print(f"{son} ning kvadrati {son**2} ga teng")

# CONTINUE OPERATORI
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")

# misol - 2
son = 0
while son<10:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)