# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
book = 'Sevimli kitobingizni kiriting'
book += '(kitoblsringizni kiritib bo`lganizdan so`ng "stop" deb to`xtating dasturni.): '
while True:
    books = input(book)
    if books == 'stop':
        break
print("Rahmat")