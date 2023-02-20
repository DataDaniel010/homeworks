import os
from os import path

'''
(По практики не надо запариваться как я показывал на уроке. 
Достаточно будет просто написать if-elif-else для каждой команды)
Написать программу, которая будет постоянно считывать
ввод пользователя и обрабатывать его команды как это делает терминал 
Команды, которые нужно обработать:
1) ls - вывести все папки и файлы текущей директории
2) ls path - вывести все папки и файлы директории path
3) cd path - переместиться в директорию path
4) pwd - вывести путь до текущей директории
5) mkdir name - создать директорию
6) touch name - создать файл
7) rm name - удалить файл
8) rm -rf - удалить директорию и всё, что внутри нее
'''
commands = ['ls', 'ls path', 'cd path', 'pwd', 'mkdir name', 'touch name', 'rm name', 'rm -rf', 'stop']
while True:
    command = input('Enter your command: ')    
    if command not in commands:
        print(f'dude: command not found: {command}')
    elif command == 'ls':
        print(os.listdir(path="."))
    elif command == 'ls path':
        print(os.listdir(path=input("write directory's name and path: ")))
    elif command == 'cd path':
        os.chdir(path=input("write path: "))
    elif command == 'pwd':
        print(os.path.abspath(path="."))
    elif command == 'mkdir name':
        os.mkdir(path=input("write directory's name: "))
    elif command == 'touch name':
        with open('new file.txt', 'w') as f:
            pass
    elif command == 'rm name':
        os.remove(path=input("write path to file: "))
    elif command == 'rm -rf':
        os.rmdir(path=input("write path to directory: "))
    elif command == 'stop':
        # для остановки цикла
        break
    continue