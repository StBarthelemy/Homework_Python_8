
from random import *
import json
Phone_book={}

def save():
    with open("contact.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(Phone_book, ensure_ascii=False))
    print("Контакт сохранен")

def load():
    with open("contact.json", "r", encoding="utf-8") as fh:
        Phone_book= json.load(fh)
    return Phone_book

    

while True:
    command = input("Введите команду: ")

    if command == "/add":
        name = input("Введите имя нового контакта: ",)
        number0 = input("Введите 1й номер: ",)
        number1 = input("Введите 2й номер: ",)
        bith_day = input("Введите ДР: ",)
        mail = input("Введите email: ",)
        Phone_book[name] = {"phone_numbers": [number0, number1], "birth_day": bith_day, "email": mail}
    elif command == "/all":
        print ("Список всех контактов")
        print(Phone_book)
    elif command == "/find":
        name = input ("Введите имя по контакту которого ищете: ")
        if name in Phone_book:
            print(Phone_book[name])
        else:
            print("Контакт не найден")
    elif command == "/save":
        save()
        print("Сохранение контактов прошло успешно")
    elif command == "/load":
        Phone_book = load()
        print("Загрузка контактов прошла успешно")
    elif command == "/delete":
        name = input ("Введите данные по контакту которого ищете и хотите удалить: ")
        if name in Phone_book:
            del Phone_book[name]
    elif command =="/edit":
        name = input ("Введите данные по контакту данные которые вы хотите найти и изменить : ")
        data = input("на какие данные мы меняем ")
        for name in Phone_book.values():
            name = data

                    

            # for data in Phone_book[name] :
            #     save
            # if name == data:
            #     name1 = input("Введите имя контакта: ",)  
            #     Phone_book[name] = Phone_book[name1]

            # elif Phone_book[name] == data:
            #     number3 = input("Введите новый номер контакта : ",)
            #     Phone_book[value1] = number3

            # elif Phone_book[name]["phone_numbers"[number1]] == data:
            #     number4 = input("Введите 2 номер  контакта: ",)
            #     Phone_book[name]["phone_numbers"[number1]] = number4

            # elif bith_day == data:
            #     data_b = input("Введите дату рождения контакта: ",)
            #     Phone_book[name]["birth_day"[bith_day]] = data_b

            # elif mail == data:
            #     mail1 = input("Введите почту контакта: ",)
            #     Phone_book[name]["email": [mail]] = mail1

            # save()
        