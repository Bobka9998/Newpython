# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def yosh_hisoblash(name, age, this_year=2022):
  """ Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya. """
  print(f'{name.title()} siz {this_year-age} yilda tug`ulgansiz.')

ism = input("Ismmizgizni kiriting: ")
yosh  = int(input("Yoshingizni kiriting: "))
yosh_hisoblash(ism,yosh)