# mahsulatlar = {
#             'olma': 12000,
#             'anor':10000,
#             'nok':5000,
#             'banana':14000
# }

# list = ['olma', 'anor', 'nok', 'banana']

# for key in mahsulatlar.keys():
#   print(key)

# for key in mahsulatlar:
#   print(key)

# for value in sorted(list):
#   print(value.title())

a = {1, 2, 3, 4, 5, 6}
b= {7,8,9,10,11,12}
c =a|b
d = a.union(b)
print(c)
print(d)

l = {1,2,3,4,5}
k = {1,2,5,6,7,8,9}
p = l&k # ikkala to`plamdagi bir xil elementlar chop etish usuli
f = l.intersection(k)
print(f'{p},\n{f}')
