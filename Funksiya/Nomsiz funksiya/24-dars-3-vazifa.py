### random moduli ichidagi sample funksiyasi yordamida 0 dan 1000 gacha sonlar oralig'idagi tasodifiy 10 ta sonlar ro'yxatini hisoblang.

from random import sample as s
sonlar = list(range(0,1000))
c = s(sonlar,10)
print(c)

# map() va lambda funksiya yoradamida sonlarning kvadratini hisoblang

kv = list(map(lambda x:x*x,c))
print(kv)

# filter() va lambda funksiya yordamida ro'yxatdan toq son ajratib oling

toq_son = list(filter(lambda x:x%2!=0,c))
print(toq_son)