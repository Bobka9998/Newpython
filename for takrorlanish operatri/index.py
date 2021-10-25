# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['ali', 'vali', 'jasur', 'otojon', 'donyor', 'xasan', 'umid']
for ism in ismlar:
    print('Salom', ism.title(), 'ishlaring qalay')
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print(f'Ro`yxat {len(ismlar)} marta takrorlandi')
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
sonlar= list(range(11,100,2))
for son in sonlar:
    print(f"{son} ning kubi {son**3} ga teng")
print(f'for {len(sonlar)} marta takrorlandi\n')
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
filmlar = []
print("sevimli 5 ta filmizni kiriting")
for film in range(5):
    filmlar.append(input(f"{film+1} sevimli filmingizni kiriting: "))
print(f"Siz yoqtirgan filmlar ro`yxati:\n{filmlar}")
# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_insonlar = int(input(f"Bugun siz nechta ison bilan suhbatlashdiz: "))
insonlar = []
for inson in range(n_insonlar):
    insonlar.append(input(f"{inson+1}-suhbatlashgan insoningiz: "))
print(f"Siz suhbatlashgan insonlar {len(insonlar)}ta ular:")
print(insonlar)