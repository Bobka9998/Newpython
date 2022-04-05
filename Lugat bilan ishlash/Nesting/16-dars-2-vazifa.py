# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

alisher = {
                  'ism':'Alisher Navoiy',
                  't_joy':'hirot',
                  't_yil':1441,
                  'v_yil':1501,
                  'asarlar':['xamsa', 'hayrat ul-abror', 'farhod va shirin','layli va majnun']
}
qodiriy = {
                  'ism':'Abdulla qodiriy',
                  't_joy':'toshkent',
                  't_yil':1441,
                  'v_yil':1938,
                  'asarlar':['o`tkan kunlar', 'mehrobdan chayon','obid ketmon', 'juvonboz']
}
usmon_nosr = {
                  'ism':'usmon nosir',
                  't_joy':'namangan',
                  't_yil':1912,
                  'v_yil':1944,
                  'asarlar':['mehrim', 'quyosh bilan suhbat', 'naxshon', 'traktorobod']
}
zulfiya  = {
                  'ism':'zulfiya isroilova',
                  't_joy':'uzbekiston',
                  't_yil':1915,
                  'v_yil':1996,
                  'asarlar':['mehrim', 'quyosh bilan suhbat', 'naxshon', 'traktorobod']
}

shaxslar = [alisher, qodiriy, usmon_nosr, zulfiya]

for shaxs in shaxslar:
  ism = shaxs['ism']
  asarlar = shaxs['asarlar']
  print(f"{ism.title()} ning mashxur asarlari:")
  for asar in asarlar:
    print(f'{asar.title()}')