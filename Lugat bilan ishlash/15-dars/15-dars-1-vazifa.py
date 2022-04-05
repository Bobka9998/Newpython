# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
l_python = {
            'boolean':'mantiqiy qiymat',
            'float':'o`nlik son',
            'for':'biror bir amalni qayta-qayta bajarish tsikli',
            'if':'shartlarni tekshirish operatori',
            'integer':'butun son',
            'str':'mantli yozuv',
            'list':'ro`yxat',
            'lower':'barcha harflarni kichik bilan chiqaradi',
            'title':'barcha so`zdagi birinchi harfni katta bilan chiqaradi',
            'capitalize':'faqat birinchi harfni katta bilan chiqaradi',
            'upper':'barcha harflarni katta bilan  chiqaradi'
            }
for key, value in sorted(l_python.items()):
  print(f' Kalit: {key.title()}.\nQiymat: {value.capitalize()}.')