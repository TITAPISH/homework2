immutable_var = 1,2,'a','b'
print(immutable_var)

immutable_var = 1,2,'a','b'
print(immutable_var)
#immutable_var [0] = 5 "Не поодерживает обращение по элементам"

mutable_list = [1, 2, 'a', 'b']
mutable_list.append('Modified')
print(mutable_list)
