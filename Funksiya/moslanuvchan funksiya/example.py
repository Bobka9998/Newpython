### *args USULI: Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa, va parametrlar yagona qiymatlar ko'rinishida uzatilsa, funksiya yaratishda argumentdan avval yulduzcha qo'yiladi (*arguments). Quyidagi misolni ko'raylik. summa()nomli funksiyamiz istalgancha sonlarni qabul qilib oladi, va ularning yi'gindisi hisoblaydi:

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi


print(summa(2,5,9,8,7,5,555,454))


# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)

#
# print(summa(2,5,9,8,7,5,555,454))


## *args usulida, bacha uzatilgan parametrlar (bir dona bo'lsa ham) funksiya ichida o'zgarmas ro'yxatga (tuple) joylanadi. Bundan kelib chiqib, yuqoridagi funksiyamizni yanada soddalashtirib yozishimiz mumkin:

## Agar funksiya bir nechta argument qabul qilsa, *args argument doim oxirida yoziladi:


# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)

#
# print(summa(1,5,8))