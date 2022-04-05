### Modulni chaqirib olish


import avto_info_mod
avto1 = avto_info_mod.avto_info('GM','Malibu','Qora','avtomat','2020','40000')
avto_info_mod.info_print(avto1)


### Modulga qisqa nom berish

import avto_info_mod as aim # modul nomini "as" yordamida kichraytirdik ya`ni avto_info_mod >>> aim
avto2 = aim.avto_info('KIA','D343','Qora','avtomat','2020','50000')
aim.info_print(avto2)

###  Modul ichidan ma`lum bir funksiyalarni chaqirib olish. FROM bilan Modul bir marta murojat qilinadi .

from avto_info_mod import avto_info, info_print
avto3 = avto_info('Lada','Xray',"malla",'avtomat',2022,18000)
info_print(avto3)

### Funksiyaga qisqa nom berish.

from avto_info_mod import avto_info as ai, info_print as ip
avto3 = ai('Lada','Xray',"malla",'avtomat',2022,18000)
ip(avto3)

### Modul ichidagi barcha funksiyalarni chaqirib olish.

from avto_info_mod import *
avto3 = avto_info('Lada','Xray',"malla",'avtomat',2022,18000)
info_print
