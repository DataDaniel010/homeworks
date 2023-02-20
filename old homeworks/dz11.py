'''
1) Название: создание класса пиво

Задача: разработать класс, который представляет собой экземпляр пива.

Функциональные требования: 
• Класс должен иметь атрибуты «Название», «Объем» и «IBU», которые 
должны присваиваться инициализатору при создании экземпляра класса;
• Класс должен иметь метод «Сгонять», который возвращает строку в зависимости от значения «IBU»:
 - Если «IBU» меньше 10 – «Слабое пиво»;
 - Если «IBU» меньше 30 – «Среднее пиво»;
 - В противном случае – «Крепкое пиво»;
• Класс должен иметь метод «Представление», возвращающий строку в виде «название пива (объем)»;
• Класс должен иметь метод «Оценка», возвращающий строку в зависимости от значения «IBU»:
 - Если «IBU» меньше 10 – «Очень сладкое пиво»;
 - Если «IBU» меньше 30 – «Отличное пиво»; 
 - В противном случае – «Очень горькое пиво»;

Нефункциональные требования:
• Код должен быть простым и читаемым;
• Использовать имена переменных и функций, соответствующие их функциям;
• Использовать правильные практики ООП.

2) Задача на наследование:
1. Цель
Создание классов для представления сущностей "Барби" и "Кукла Барби" на языке Python с 
использованием принципов ООП наследования.

2. Требования
2.1. Необходимо создать два класса: "Барби" (Barbie) и "Кукла Барби" (BarbieDoll).
2.2. Класс "Барби" должен содержать информацию о внешнем виде, ментальности и характере Барби.
2.3. Класс "Кукла Барби" должен наследовать все свойства класса "Барби" и также содержать 
информацию о материале, из которого она сделана (пластик, бархат и т.д.), о типе производства (массовое или ограниченное), цвете, 
дополнительных атрибутах и деталях (настроечные глаза, тканевые юбки и т.п.).
2.4. Для каждого класса требуется создать методы, которые позволят получать и изменять значения атрибутов.

3. Инструкция
3.1. Создайте два класса: "Барби" и "Кукла Барби".
3.2. В класс "Барби" добавьте атрибуты для представления ее внешнего вида, ментальности и характера.
3.3. В класс "Кукла Барби" добавьте атрибуты, такие как материал, из которого она сделана, тип 
производства, цвет и дополнительные атрибуты и детали.
3.4. Укажите для каждого класса методы для получения и изменения атрибутов.
3.5. Убедитесь, что класс "Кукла Барби" наследует все атрибуты и методы класса "Барби".
'''

class Pivo:

    def __init__(self, name, volume, IBU) -> None:
        self.name = name
        self.volume = volume
        self.IBU = IBU
        
    # метод Сгонять:
    def sgon(self):
        if self.IBU <= 10:
            print('weak beer')
        elif 10 < self.IBU  <= 30:
            print('medium beer')
        else:
            print('strong beer, good choice')  
    
    # метод представление
    def show(self):
        print(f'"{self.name}({self.volume})"')
    
    # метод оценка
    def rating(self):
        if self.IBU <= 10:
            print('very sweet beer')
        elif 10 < self.IBU  <= 30:
            print('great beer')
        else:
            print('very bitter beer') 


class Barbie:

    def __init__(self, appearance, mentality, character) -> None:
        self.appearance = appearance
        self.mentality = mentality
        self.character = character

    def print_info(self):
        print(self.appearance, self.mentality, self.character)

    # актуальная внешность
    def actual_appearance(self):
        print(f'Actual appearance: {self.appearance}')
        
    # изменение внешности
    def ch_appearance(self, changes=''):
        changes = input('write new appearance: ')
        print(f'\nOld appearance: {self.appearance}')
        self.appearance = changes
        print(f'New appearance: {changes}')

    # актуальная ментальность
    def actual_mentality(self):
        print(f'Actual mentality: {self.mentality}')

    # изменение ментальности
    def ch_mentality(self, changes=''):
        changes = input('write new mentality: ')
        print(f'\nOld mentality: {self.mentality}')
        self.mentality = changes
        print(f'New mentality: {changes}')

    # актуальный характер
    def actual_character(self):
        print(f'Actual character: {self.character}')

    # изменение характера
    def ch_character(self, changes=''):
        changes = input('write new character: ')
        print(f'\nOld character: {self.character}')
        self.character = changes
        print(f'New character: {changes}')
        



# b1 = Barbie('blond', 'clever', 'nice')
# b1.ch_character()
# b1.actual_character()


class BarbieDoll(Barbie):
    
    def __init__(self, appearance, mentality, character, material, production, colour, features) -> None:
        super().__init__(appearance, mentality, character)
        self.material = material
        self.production = production
        self.colour = colour
        self.features = features

    # актуальный материал
    def a_material(self):
        print(self.material)
    
    # изменение материала
    def c_material(self, other):
        self.material = other
        print(f'New material is {other}')
    
    # актуальное производство
    def a_production(self):
        print(self.production)
    
    # изменение производства
    def c_production(self, other):
        self.production = other
        print(f'New production is {other}')
    
    # актуальный цвет
    def a_colour(self):
        print(self.colour)
    
    # изменение цвета
    def c_colour(self, other):
        self.colour = other
        print(f'New colour is {other}')
    
    # актуальные особенности
    def a_features(self):
        print(self.features)
    
    # изменение особенностей
    def c_features(self, other):
        self.features = other
        print(f'New features are {other}')

# b2 = BarbieDoll('white', 'serious', 'silly', 'plastic', 'single', 'white', 'hypoallergenic plastic')
# b2.actual_appearance()
# b2.a_features()

