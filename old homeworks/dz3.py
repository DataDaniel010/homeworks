'''
## **Задачи:**

### **Задача 1:**

Врач рекомендует принимать выписанное лекарство по чётным дням. Напишите программу, которая
принимает от пользователя число и выводит на экран соответствующее напоминание: 
чётный день - пить лекарство, нечётный - не пить

<br/> 

### **Задача 2:**

Однажды студент решил написать программу, определяющую модуль числа. 
Помогите ему в этом: напишите скрипт, печатающий модуль введённого числа.

Образец работы программы:
```
Введите число: 6
Ввели: 6, модуль: 6

Введите число: -6
Ввели: −6, модуль: 6
```

<br/> 

### **Задача 3:**

Пользователь хочет снять деньги со счёта с помощью банкомата. 
В банкомате остались только купюры с минимальным номиналом 200 рублей. 
Напишите программу, проверяющую возможность выдачи запрашиваемой суммы.


<br/> 

### **Задача 4:**

Напишите программу, принимающую три числа и печатающую максимальное из них.
(При решении без доп. переменных +1 балл)

<br/> 

### **Задача 5:**

Сотрудник магазина получает надбавку к зарплате, если выполняет норматив по продажам. 
- Если суммарная стоимость проданных товаров превышает 50 000 рублей, то надбавка максимальная.
- Если суммарная стоимость проданных товаров от 10 000  по 50 000 включительно, то надбавка - половина от максимальной
- Если продавец не смог продать и на 10 000, то надбавки нет вовсе. 

Напишите программу, которая выводит надбавку в зависимости от указанной суммы.

<br/> 

### **Задача 6:**

Напишите программу, которая определяет значение функции Y, в зависимости от введённого числа X:
![task](task6.png "Задание")

<br/> 

### **Задача 7:**

Небходимо распределить награды за участие в студенческой олимпиаде по информатике.
Первые 20 человек из рейтинга получают "Диплом победителя".
Те из победителей, кто набрал более 95 баллов, получают "Денежный приз".
Остальные участники получают "Сертификат участника".
Программа должна принимать результаты участника и писать, на какую награду участник может 
рассчитывать.


Примеры:
```
Ваше место в рейтинге: 6
Ваш балл: 99

Ваша награда: "Диплом победителя"!
Также Вы получаете "Денежный приз"!


 
Ваше место в рейтинге: 16
Ваш балл: 94

Ваша награда: "Диплом победителя"!

 
 
Ваше место в рейтинге: 36

Ваша награда: "Сертификат участника"!
```

<br/> 

### **Задача 8:**
Напишите программу, которая получает на вход число и проверяет, трёхзначное оно или нет. 

Числа типа "−100" тоже считаются двузначными. 

Выполните задание, используя не более одного оператора if-elsе и не используя elif.

<br/> 

### **Задача 9:**

Есть три целых числа. Определите сколько из них совпадающих. 
*(См. первую рекомендацию в требованиях к выполнению)*

Программа должна вывести:
- 0, если совпадений нет
- 2, если есть два совпавших
- 3, если все совпадают

'''
current_date = int(input('Введите сегондняшнее число: '))
if current_date % 2 == 0:
    print('Пить лекарство')
else:
    print('Не пить лекарство')


num = int(input('Введите число: '))
if num >= 0:
    print(f'Ввели: {num} модуль: {num}')
elif num < 0:
    num1 = num * -1
    print(f'Ввели: {num} модуль: {num1}')


money = int(input('Введите сумму, которую хотите снять: '))
if money % 200 == 0 or money % 500 == 0 or money % 1000 == 0:
    print('Банкомат способен выдать такую сумму')
else:
    print('Банкомат не способен выдать такую сумму')


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1 > num2 and num1 > num3: 
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)


profit = int(input('Введите суммарную сумму проданных товаров: '))
if profit > 50000:
    print('Вы получаете максимальную надбавку')
elif 10000 <= profit <= 50000:
    print('Вы получаете половину от максимальной надбавки')
elif profit < 10000:
    print('Плохо продавали! Без надбавки в этом месяце.')


x = int(input('Введите число х: '))
if x <= 0:
    y = x**2 - 1
    print(f'y = {y}')
elif 0 < x < 2:
    y = x
    print(f'y = {y}')
elif x >= 2:
    y = 2*x - 2
    print(f'y = {y}')


rating = int(input('Какое место в рейтинге занял участник? '))
score = int(input('Сколько баллов набрал участник? '))
if 0 < rating <= 20 and score > 95:
    print(f'Ваше место в рейтинге: {rating} \nВаш балл: {score} \nВаша награда "Диплом победителя" \nТакже вы получаете "Денежный приз"')
elif 0 < rating <= 20 and score <= 95:
    print(f'Ваше место в рейтинге: {rating} \nВаш балл: {score} \nВаша награда "Диплом победителя"')
else:
    print(f'Ваше место в рейтинге: {rating} \nВаша награда "Сертификат участника"')


num = int(input('Введите число: '))
if 99 < num <= 999 or -999 <= num < -99:
    print(f'Число {num} трехзначное')
else:
    print(f'Число {num} не трехзначное))')


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1 != num2 and num1 != num3 and num2 != num3:
    print(f'Совпадений 0')
elif (num1 == num2 and num1 != num3) or (num1 == num3 and num1 != num2):
    print(f'Совпадений 2')
elif num1 == num2 and num1 == num3:
    print(f'Совпадений 3')
