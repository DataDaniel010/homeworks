'''
Задача 1:
Когда Антон прочитал «Войну и мир», ему стало интересно, 
сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, 
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и 
выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) 
в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово​ должно выводиться только один раз
'''
lst_string = input('write string: ').lower().split()
res_words = []
for word in lst_string:
    if word not in res_words:
        res_words.append(word)
for w in res_words:
    print(f'слово {w} количество {lst_string.count(w)}') 




