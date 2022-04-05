# meva = {'apple':'olma', 'ism':'akbar', 'familya':'qalandarov', 'yosh':'24', 'tug`ulgan yil':'1995'}
# print(meva['ism'].title())
python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))