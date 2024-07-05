my_dict = {'Maxim':1988, 'Sonya':2018}
print(my_dict)
print(my_dict['Sonya'])
print(my_dict.get('Sveta'))
my_dict.update({'Sasha':1987,
                'Vika':1990})
del my_dict['Vika']
print(my_dict)

my_set = {1,2,3,3,2,2,1, 'apple','room','apple'}
print(my_set)
my_set.update([32,567,])
my_set.remove(32)
print(my_set)
