##### Funksiya oddiy


def salom_ber():
  """ Salom beruvchi funksiya"""
  print('Assalomu Alaykum')
print('\n')


##### Qiymat qabul qiluvchi qiymat

def salom_ber(name):
  '''Foydalanuvchidan salom beruvchi funksiya''' # <<< docstring
  print(f'Assalomu Alaykum, hurmatli {name.title()}!')
salom_ber("bobur")
print(salom_ber.__doc__) # Docstring ekranga chiqarish usuli
print('\n')

##### Funksiyaga bir nechta argument uzatish

def toliq_ism(name, surname):
  """Ism va Familyani chamlab chiqaruvchi fuksiya"""
  print(f'Foydalanuvchining ismi: {name.title()}.\n'
        f'Foydalanuvchining familyasi: {surname.title()}.')
toliq_ism('iso','isoqov')
toliq_ism('hasan','yusufov')
print(toliq_ism.__doc__)

print('\n')

##### Fuksiyada standart qiymat berish

def yosh_hisobla(tugulgan_yil, joriy_yil=2022):
  """yosh hisoblash funksiyasi"""
  print(f'Siz {joriy_yil-tugulgan_yil} yoshdasiz.')

yosh_hisobla(1995,2021)
yosh_hisobla(1995)  # <<<< bu standart qiymat hisoblanadi

print('\n')

###### Xatolikni topish

def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

tyil =int(input("Tug'ilgan yilingizni kiriting: "))
yosh_hisobla(tyil)

print('\n')

def yosh_hisobla(tugilgan_yil, joriy_yil):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1993,2022)

print('\n')

def salom_ber(name):
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!",name.title())
salom_ber('hasan')

print('\n')


def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
toliq_ism('olim ','hakimov')
