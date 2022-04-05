# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
buyurtmalar = ['olma', 'anor', 'sabzi', 'pamidor', 'nok']
bozorlik ={
            'olma': 1200,
            'guruch':9000,
            'banana':6668,
            'sabzi': 3000,
            'piyoz': 4000,
            'kartosh': 4000,
            'pamidor':87485
}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in bozorlik.keys():
        narh = bozorlik[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")