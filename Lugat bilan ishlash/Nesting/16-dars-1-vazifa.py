    # Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
xorazmiy ={
                 'ism':'Abu Abdulloh Muhammad ibn Muso al Xorazmiy',
                 't_joy':'xiva',
                 't_yil':783,
                 'v_yil':850
}
beruniy = {
                 'ism':'Abu Rayhon Beruniy Muhammad ibn Ahmad',
                 't_joy':'xorazm',
                 't_yil':973,
                 'v_yil':1048
}
manguberdi = {
                 'ism':'Jaloliddin Manguberdi',
                 't_joy':'xorazm',
                 't_yil':1198,
                 'v_yil':1231
}
alisher = {
                 'ism':'Alisher Navoiy',
                 't_joy':'hirot',
                 't_yil':1441,
                 'v_yil':1501
}

shaxslar = [xorazmiy, beruniy, manguberdi, alisher]
for shaxs in shaxslar:
    ism = shaxs['ism']
    t_yil = shaxs['t_yil']
    t_joy = shaxs['t_joy']
    v_yil = shaxs['v_yil']
    print(f'{ism} {t_yil}-yil {t_joy}da tug`lgan. {v_yil - t_yil}-yil umr ko`rganlar.')
