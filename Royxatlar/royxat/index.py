#  // Ro`yxatlar
davlatlar = ['uzbekiston', 'qozog`iston', 'tojikiston', 'misr', 'rossiya', 'turkiya', 'turkmaniston', 'aqsh']
print(davlatlar)
#  // sonli ro`yxatlar va arifmetik amallar
narxlar = [ 1250, 2545874, 52548569, 526254, 7894568585 ]
print(narxlar)
print(narxlar[1] + narxlar[3])
print(narxlar[0] - narxlar[4])
print(narxlar[4] / narxlar[0])
print(narxlar[1] * narxlar[3])
print(narxlar[-1])
narxlar = str(narxlar[1])
print('Ro`yxat oxiri ' + narxlar[-1])
#  // Elementlarni qo`shish , o`chirish va o`zgartirish
# element o`zgartirish
qiymat = [12000, 13000, 25000, 14000]
qiymat[0] = 15000 #1-qiymatni 15000 ga o`zgartiramiz
qiymat[1] = 17000 #2-qiymatni 17000 ga o`zgartiramiz
qiymat[2] = qiymat[2] + 5000 #3-qiymatga 5000 qo`shamiz
print(qiymat)
cars = ['bmw', 'audi', 'mers', 'tesla', 'kia', 'reno']
cars[0] = 'tico'
print(cars)
# yangi element qo`shish
mevalar = ['anjir', 'anor', 'uzum', 'behi', 'hurmo']
mevalar.append('olma')  # .append() ro`yxat oxiriga element qo`shish
mevalar.insert(2, 'bodom') # .insert() ro`yxatning istalgan joyiga yangi element qo`shadi
mevalar.insert(0, 'shaftoli')
print(mevalar)
# elementni ochirish
ranglar = ['qizil', 'yashil', 'ko`k', 'qora', 'oq', 'sariq']
del ranglar[1] # elementni o`chirish uchun "del" dan foydalanamizva indeksni kiratamiz, 2-qiymatni (yashilni) ochiramiz
print(ranglar)
# Elementni qiymati bo`yicha o`chirish esa ".remove()" dan foydalanamiz
ismlar = ['donyor', 'jasur', 'ulug`bek', 'otojon', 'nodir', 'xasan', 'sherbek']
ismlar.remove('sherbek') # bur yerda "sherbek" qiymatni o`chirib tashlaymiz
print(ismlar)
# agarda ro`yxat ichida 2 ta va undan ko`p qiymat bo`lsa ".remove()" birinchi qiymatni o`chiradi
# // Elementni sug`urib olish
bozorlik = ['yog`', 'un', 'shakar', 'tuz', 'zira', 'piyoz', 'banan']
mahsulot = bozorlik.pop(2 ) # 3-elementni sug`urib olamiz
print('Men ' + mahsulot + ' sotib oldim')
print('Olinmagan mahsulotlar: ', bozorlik)
# Agarda ".pop()"ga indeks berilmasa u ro`yxatdagi oxirgi qiymatni sug`irib oladi
# Ro`yxatdan elment nomi bilan sug`irib olish uslibi.
sinflar = ['6a', '7a', '8a', '9a', '10a']
sinf_with = sinflar.index('8a')
sinf = sinflar.pop(sinf_with)
print(sinf)
print(sinflar)
