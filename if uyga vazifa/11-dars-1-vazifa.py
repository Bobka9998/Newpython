# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
son = int(input('Juft son kirirting: '))
if son < 0:
  print('Kiritgangan soningiz "Manfiy son" iltimos "Juft son" kiriting!')
elif son%2:
  print('"Bu juft son emas"')
else:
  print("'Rahmat!'")