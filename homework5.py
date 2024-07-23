immutable_var = (1, 2, 3, 'a', True)
print(immutable_var)
immutable_var_1 = 1, 2, 3, 'a', True
print(immutable_var_1)
immutable_var_2 = tuple([1, 2, 3, 'a', True])
print(immutable_var_2)
#кортеж сам по себе не изменяем, упорядочен, и хранит объекты разных видов
#элементы кортежа могут быть изменены
mutable_list = [1, 2], 3, 'a', True
print(mutable_list)
mutable_list[0][0] = 2#вытаскиваем первый элемент и меняем его на 2-ку
print(mutable_list)