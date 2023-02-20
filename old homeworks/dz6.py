'''
Задача 1:
Пользователь вводит длину стороны квадрата N и символ CH. \
     Программа должна вывести с помощью символа CH квадрат со стороной N

Задача 2:
Сгенерировать рандомную последовательность из 5 чисел. Диапазон последовательности от 1 до 100. 
Если все числа в последовательности больше 50, вывести True, в ином случае False

Задача 3: 
Задачу начать решать с пустого списка:
lst = []
Папа написал Саше список продуктов (молоко, огурцы, пиво, рыбка) 
и бабушка тоже попросила купить некоторые продукты (чай, сахар, сухарики).
Мама увидела список и сказала вычеркнуть пиво и рыбку
Помоги Саше сформировать единый список покупок и посчитать сколько 
пунктов содержит общий список покупок

Задача 4:
Есть список. пользователь вводит число. Нужно определить, 
есть ли это число в списке 

Задача 5:
Есть список и число, которое ввел пользователь
посчитать сколько раз это число встречается в списке

'''
# Task1
# length = int(input('write length '))
# symbol = 'CH'
# for i in range(1, length + 1):
#     print(symbol * length)


# Task2
import random
lst = [random.randint(1, 101) for i in range(5)]
flag = False
for j in lst:
    if not j > 50:
        flag = True
        print(False)
        break                
if flag == False:
    print(True)

print('-------------------------------')

# Task3
lst = []
dad_lst = ['молоко', 'огурцы', 'пиво', 'рыбка']
dad_lst.append('чай')
dad_lst.append('сахар')
dad_lst.append('сухарики')
# grma_lst = ['чай', 'сахар', 'сухарики']
lst = dad_lst # или lst = dad_lst + grma_lst
print(lst)
# коррекция от мамы
lst.remove('пиво')
lst.remove('рыбка')
print(lst)
# узнаем количество элементов в списке
num = len(lst)
print(num)

print('-------------------------------')

# Task4
# lst = [random.randint(1,1000) for _ in range(1000)]
# num = int(input('write number '))
# if num in lst:
#     print('here is it')
# else:
#     print('nope')


# Task5
# lst = [random.randint(1,100) for _ in range(1000)]
# num = int(input('write number '))
# how_many = 0
# for i in lst:
#     if num == i:
#         how_many += 1
# print(f'Число {num} встречается в списке {how_many} раз')

