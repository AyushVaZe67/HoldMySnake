capitals = {'USA':'Washington DC','India':'New Delhi','Japan':'Tokyo','Russia':'Moscow','Peru':'Lima'}

print(capitals.get('USA'))

capitals.update({'Germany':'Berlin'})
capitals.update({'India':'Mumbai'})

print(capitals)

capitals.pop('Japan')

# print(capitals.keys())
#
# print(capitals.values())

print(capitals.items())

for key,value in capitals.items():
    print(f'{key} : {value}')