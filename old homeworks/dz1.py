# ТО ЧТО НУЖНО БЫЛО СДЕЛАТЬ
# ### **Задача 1:**
# Исправьте ошибки в  программе:
# ```python
# name = 'Ivan'
# surname = Petrov
# print('name, surname, любит покушать.')
# ```

# Образец работы программы:
# ```
# Ivan Petrov любит покушать
# ```
# <br/> 

# ### **Задача 2:**
# Исправьте программу так, чтобы в результате выводился текст, указанный в "результате работы программы":
# ```python
# r = 'Red'
# g = 'Green'
# b = 'Blue'

# print(r, g, b, b + b + g, r)
# ```
# Необходимый результат работы программы:
# ```
# Green Red Blue RedRedGreen BlueGreen Green
# ```

# <br/> 

# ### **Задача 3:**

# Напишите программу, которая запрашивает у пользователя данные и выводит их на экран как в образце (данные укажите свои):

# ```
# Ваше имя: Илья
# Ваша фамилия: Шутов
# Укажите Ваше любимое блюдо: мармелад
# Пользователь Илья Шутов любит есть мармелад.
# Порадуемся за него!
# ```

# <br/> 

# ### **Задача 4:**

# К Вам за помощью обратился железнодорожный вокзал Екатеринбурга. Вас просят написать программу, которая запрашивает у 
# пользователя пункт отправления и пункт прибытия, после чего печатает их в одну строчку через тире.

# <br/> 

# ### **Задача 5:**

# Допишите программу так, чтобы при повторном выводе значения переменных поменялись местами. Исходные строки не менять.
# (Есть несколько способов)
# ```python
# a = input('First word: ')
# b = input('Second word: ')
# print(a, b)

# # Здесь Ваш код

# print(a, b)
# ```
# Образец работы программы:
# ```
# First word: Hello!
# Second word: Bye!
# Hello! Bye!
# Bye! Hello!
# ```

# <br/> 

# ### **Задача 6:**

# Напишите программу, которая запрашивает у пользователя параметры трапеции: длины оснований и высоту, после чего выводит 
# площадь такой трапеции.

# <br/> 

# ### **Задача 8:**

# Напишите программу, которая запрашивает у пользователя два числа, складывает последние цифры чисел и выводит ответ на 
# экран.

# Пример работы программы:
# ```
# Введите первое число: 105
# Введите второе число: 101
# Ответ: 6
# ```

# <br/> 

### **Задача 8:**

# Напишите программу, которая запрашивает у пользователя четырёхзначное число и выводит число "наоборот". Переменную, 
# в которую записали изначальное число, не изменять.

# Пример работы программы:
# ```
# Введите число: 1234
# # Обратное число: 4321
# ```

### ***Задача 9:**

# Допишите программу. Программа принимает два числа и выводит их по порядку. При повторном выводе значения переменных 
# должны поменяться местами. Исходные строки не менять.
# Решите эту задачу без использования переменных и "синтаксического сахара".
# ```python
# a = input('First number: ')
# b = input('Second number: ')
# print(a, b)

# Здесь Ваш код

# print(a, b)




# ВЫПОЛНЕНИЕ ДЗ

# Задача 1
# name, surname = 'Ivan', 'Petrov'

# print(name, surname, 'любит покушать.')

# Задача 2
# r, g, b = 'Red', 'Green', 'Blue'

# print(g, r, b, r + r + g, b + g, g)

# Task 3
# first_name = input('Your name is: ')
# surname = input('Your surname is: ')
# favourite_food = input('Indicate your favourite food: ')

# print('User', first_name, surname, 'likes to eat', favourite_food)
# print('Lets be happy for him!')

# Task 4
# point_of_departue = input('Indicate your point of departue: ')
# point_of_arrival = input('Indicate your point of arrival: ')

# print(point_of_departue + '-' + point_of_arrival)

# Task 5

# a = input('First word: ')
# b = input('Second word: ')
# print(a, b)

# c = a
# a = b
# b = c

# OR
# a, b = b, a  # множественное присваивание, переменные меняются своими местами

# print(a, b)

# Task 6
# trapezoid_height = input('Wright trapezoid height: ')
# trapezoid_height = int(trapezoid_height)
# small_base_length = input('Write small base length: ')
# small_base_length = int(small_base_length)
# large_base_length = input('Write large base length: ')
# large_base_length = int(large_base_length)

# square = (0.5 * trapezoid_height * (small_base_length + large_base_length))

# print(square)

# Task 7
# first_number = input('Enter the first number: ')
# first_number = int(first_number)
# second_number = input('Enter the second number: ')
# second_number = int(second_number)

# c1 = first_number % 10
# c2 = second_number % 10

# sum = c1 + c2 
# print('Answer is: ', sum)

# Task 8 
# a = int(input('Write a four digit number: '))
# b = a 
# c = b % 10
# b = b // 10
# d = b % 10
# b = b // 10
# e = b % 10
# b = b // 10
# a1 = c*1000 + d*100 + e*10 + b

# OR

# a = int(input('Write a four digit number: '))
# b = a 
# c = b % 10
# d = (b // 10) % 10
# e = (b // 100) % 10
# b = b // 1000
# a2 = str(c) + str(d) + str(e) + str(b)

# print()



# # Task 9
# a = input('First number: ')
# b = input('Second number: ')
# print(a, b)

# a = int(a) + int(b)
# b = a - int(b)
# a = a - b

# print(a, b)






# Task 7
# number1 = int(input('Write first number: '))
# number2 = int(input('Write second number: '))
# number1 = number1 % 10
# number2 = number2 % 10
# total = (number1 + number2)
# print('Answer is: ', total)

# Task 8
# number = int(input('Write four digit number: '))
# number1 = number % 10
# number = number // 10
# number2 = number % 10
# number = number // 10
# number3 = number % 10
# number = number // 10
# total = number1 * 1000 + number2 * 100 + number3 * 10 + number
# print(total)

# a = int(input('First number: '))
# b = int(input('Second number: '))
# print(a, b)

# c = a + b
# a = c - a
# b = c - b
# print(a, b)
