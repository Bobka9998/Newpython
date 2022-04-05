print('Do`stlar ro`yxati!')
ismlar = []
n  = 1
while True:
  savol = f'{n} do`stingizni kiriting: '
  ism = input(savol)
  ismlar.append(ism)
  takrorlash = input(f'yana do`st kiritasizmi (ha/yo`q): ')
  n += 1
  if takrorlash != 'ha':
    break

print('Ro`yxat do`stlar.')
for ism in ismlar:
  print(ism.title())