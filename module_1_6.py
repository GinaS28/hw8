my_dict = {'Regina': 1999, 'Radik': 1997, 'Margo': 2020}
print('Словарь:', my_dict)
print('Год рождения Регины:', my_dict['Regina'])
print('Год рождения Данила:', my_dict.get('Daniel', 'Такого ключа нет'))
my_dict.update({'Sasha': 2000, 'Maria': 1998})
a = my_dict.pop('Sasha')
print('Удаленное значение:', a)
print('Измененный словарь:', my_dict)

my_set ={1, 2, 1, 'a', 2, 5.7, True, False, 'a', True}
print('Множество:', my_set)
my_set.add(3)
my_set.add('b')
my_set.discard(False)
print('Измененное множество:', my_set)
