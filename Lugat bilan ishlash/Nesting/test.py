m_shaxslar = {
  'matematika':{
                 'ism':' Abu Abdulloh Muhammad ibn Muso al Xorazmiy',
                 't_joy':'xiva',
                 't_yil':783,
                 'v_yil':850,
                 'fan':['matematik', 'astronom', 'geograf'],
                 'ma`lumot':' fan tarixidagi ilk qomusiy oliml'
                },
  'geografiya':{
                 'ism':'Abu Rayhon Beruniy Muhammad ibn Ahmad',
                 't_joy':'xorazm',
                 't_yil':973,
                 'v_yil':1048,
                 'fan':['astronomiya','matematika', 'geodeziya', 'geografiya','mineralogiya'],
                 'ma`lumot':'qomusiy olim'
                },
  'adabiyot':{
                 'ism':'Alisher Navoiy',
                 't_joy':'hirot',
                 't_yil':1441,
                 'v_yil':1501,
                 'fan':['adabiyot','nazm','g`azal'],
                 'ma`lumot':'davlat arbobi'
                },
  'sarkarda':{
                 'ism':'Jaloliddin Manguberdi',
                 't_joy':'xorazm',
                 't_yil':1198,
                 'v_yil':1231,
                 'fan':['mohir sarkarda'],
                 'ma`lumot':'podshox'
                }
}
for shaxs, info in m_shaxslar.items():
  print(f'{shaxs.title()} {info["ism"].title()}.'
        f"{info['t_yil']}-yil {info['t_joy']}da tug`ulgan."
        f"{info['v_yil']}da vafot etganlar."
        f"O`z davri {info['ma`lumot'].title()} bo`lib yashashgan."
        f"shu soxalarda juda kuchli bo`lishgan."
        )
  for k in info['fan']:
      print(k.upper())