# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
foydalanuvchilar = ['akbar32', 'doniyor45', 'jamoltaxi', 'liverpool99', 'uzbek96']
login = input('Yangi login tanlang: ')
if login.lower() in foydalanuvchilar:
  print('Login band, yangi login tanlang!')
else:
  print('Xush kelibsiz')
