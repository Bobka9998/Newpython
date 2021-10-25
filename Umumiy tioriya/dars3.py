# Matnlarni qo`shish uchun + operatordan foydalanamiz
ism = 'Jasur'
print("Mening ismim "  + ism)
# Ikkata o`zgaruvchi orasiga bosh joy tashlash uchun quydagicha foydalanamiz 
ism= 'Bekpo`lot'
familya= 'Baktemirov'
print(ism +' '+ familya)
# Ikki va undan ko`p ko`rinishdagi o`zgaruvchilarni birlashtirish uchun f-string (f"{mant} {mant2}") foydalanamiz
ism= 'Asad'
familya='Qayum'
ism_sharif=f"{ism} {familya}"
print(ism_sharif)
# f-stirng yordamida uzun matnlar ham yashash mumkin
fname= 'James'
lname= 'Bond'
mant= f"Salaom mening {lname}. {fname} {lname}!"
print(mant)
# title() va capitalize() , upper() metodlari
# title()
matn= 'salom hammaga'
print(matn.title())
# capitalize()
matn= 'salom hammaga'
print(matn.capitalize())
# upper
matn= 'salom hammaga'
print(matn.upper())
# stirp(), rstrip() va lstirp() metodlari
meva= "  olma  "
print("Men " + meva.strip()+ "yaxshi ko`raman")
#rstrip
meva= "  olma  "
print("Men " + meva.rstrip()+ "yaxshi ko`raman")
#lstrip()
meva= "  olma  "
print("Men " + meva.lstrip()+ "yaxshi ko`raman")

