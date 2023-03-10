'''
___
## **Задачи:**

### **Задача 1:**
Создайте две переменные с именами. 
Запишите в первую переменную имя одного человека, а во вторую — второго. 
Используя эти переменные и f-string выведите на экран текст «'имя1' делает домашнюю работу, 'имя2' решил отдохнуть» в одну строку.

<br/> 

### **Задача 2:**
Напишите программу. Программа должна запрашивать у пользователя отзыв от проведённом отдыхе, после чего выражать ему 
благодарность с указанием того, насколько длинным получился отзыв:

Пример работы программы:
```
Введите Ваш отзыв: Всё понравилось, очень здорово!
Спасибо за подробный отзыв! В нём аж 31 символ(а)!
```

<br/> 

### **Задача 3:**
Ещё раз справьте программу так, чтобы в результате выводился текст, указанный в "результате работы программы".
На этот раз напишите программу в двух вариантах: 1. С использованием f-string. 2. С использованием метода .format:
```python
r = 'Red'
g = 'Green'
b = 'Blue'

print(r, g, b, b + b + g, r)
```
Необходимый результат работы программы:
```
Green Red Blue RedRedGreen BlueGreen Green
```


<br/> 

### **Задача 4:**
Напишите программу, принимающую на проверку потенциально проблемные ФИО пользователя. 
Программа должна иправлять регистр введёных ФИО и выводить на экран корректный вариант:
```
Введите ФИО: ИВАНОВ иВаН иваныч
Исправленный вариант: Иванов Иван Иваныч
```

<br/> 

### **Задача 5:**
У нас попросили написать подпрограмму для крупного ресторанного проекта. 
Наш код должен получать с клавиатуры три блюда и корректно (с соблюдением регистра) 
добавлять их в одну строку-шаблон меню и печатать эту строку:
```
Введите первое блюдо: Борщ
Введите второе блюдо: МакароНы с ГОВЯЖЬЕЙ отбивноЙ
Введите десерт: тирамису

Блюда дня:
Первое: борщ!
Второе: макароны с говяжьей отбивноЙ!
Тирамису — на десерт!
```

<br/> 

### **Задача 6:**

Вам поручили проанализировать данные бухгалтерии за последний месяц. Оказалось, что крупные числа в базу данных были 
записаны с разделителем разрядов — запятой (1,000,000). Но Вы не знаете как работать с таким форматом чисел в python, 
поэтому перед анализом данных, Вы должны эти данные правильно подготовить.

Изучите самостоятельно принцип работы строчного метода .replace() и используйте его для преобразования чисел в понятный 
питону вид:

```
Введите число: 99,999,999.95
Рабочее число: 99999999.95
```

<br/> 

### **Задача 7:**

Заказчик прислал Вам документ с текстом:
```python
doc = От Иванова 
Кому: Петрову 
\t\t\t\t\t\tОБЪЯСНИТЕЛЬНАЯ
Я, Иванов, не сделал домашнее задание по python, поскольку моя жена, Иванова, 
попросила меня забрать из детского сада моего сына, Иванова. 
Сама она не могла, поскольку посещала доктора Иванова,
нашего однофамильца. 
В связи с этим прошу не ставить двойку мне, Иванову, и на первый раз простить!

Дата:________\t\t\t\t\tПодпись:_______/Иванов
```
Этот документ он получил от своего друга и теперь просит везде поменять фамилию друга на фамилию Заказчика 
(выбирайте на своё усмотрение).
Замените фамилию, используя изученный ранее метод и напечатайте документ на экране.
'''

name1 = 'Ivan'
name2 = 'Igor'
text = f'{name1} doing homework, {name2} decided to rest'
print(text)

review = input('Please, write a review: ')
length = len(review)
print(f'Thanks for your feedback! It has {length} symbols')

# 1
r, g, b = 'Red', 'Green', 'Blue'
print(f'{g} {r} {b} {r + r + g} {b + g} {g}')

# 2
colors = '{g} {r} {b} {r}{r}{g} {b}{g} {g}'.format(g = 'Green', r = 'Red', b = 'Blue')
print(colors)

fio = input('Введите ФИО: ')
fio = fio.title()
print(fio)

starter = input('Write the starter: ').lower()
main_course = input('Write the main course: ').lower()
dessert = input('Write the dessert: ').title()
meal = f'Your order: \n Starter: {starter}! \n Main course: {main_course}! \n {dessert} - for dessert!'
print(meal)


doc = '''От Иванова 
Кому: Петрову 
\t\t\t\t\t\tОБЪЯСНИТЕЛЬНАЯ
Я, Иванов, не сделал домашнее задание по python, поскольку моя жена, Иванова, 
попросила меня забрать из детского сада моего сына, Иванова. 
Сама она не могла, поскольку посещала доктора Иванова,
нашего однофамильца. 
В связи с этим прошу не ставить двойку мне, Иванову, и на первый раз простить!

Дата:________\t\t\t\t\tПодпись:_______/Иванов'''
doc = doc.replace('Иванов', 'Голубцов')
print(doc)