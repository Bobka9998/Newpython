# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh = int(input('Yoshingizni kiriting: '))
if yosh <= 4 or yosh >= 60:
  kirish = ('Bepul')
elif yosh < 18:
  kirish = ('10 000 so`m')
else:
  kirish = ('20 000 so`m')
print(f"Sizga kirish {kirish}. Marhamat!")