#  Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def malumot_talaba(ism,familya,**malumotlar):
  """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya"""

  malumotlar['ism']=ism
  malumotlar['familya']=familya

  return malumotlar


talaba = malumot_talaba('abu','hasanov',yoshi = 25,t_joy='samarand')
talaba1 = malumot_talaba('hasan','qadirov',yosh = 24, t_joy = 'xorazm', t_yil = 1995)
print(talaba)
print(talaba1)


# def talaba_info(ism, familiya, **kwargs):
#     kwargs['ism']=ism
#     kwargs['familiya']=familiya
#     return kwargs

# talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')



# import random as r

# d = list(range(11))
# print(d)
# print(r.shuffle(d))