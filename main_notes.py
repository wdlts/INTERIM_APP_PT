import csv
import time
from datetime import datetime
import io
import idgeneration
from searchid import idsearchdelete

csv.register_dialect('РАЗДЕЛИТЕЛЬ', delimiter=';', skipinitialspace=True)
filecontent = []
notes = []
current_datetime = datetime.now()
myFile = open('notes.csv', 'a')



def mainMenu():
    print("1. Создать заметку\n"
          "2. Просмотреть заметку\n"
          "3. Редактировать заметку\n"
          "4. Удалить заметку\n"
          "5. Выход\n")


def mainProg():
    mainMenu()

    while True:
        command = input("Выберите команду: ")
        if command == "1":
            noteHeader = input("Введите заголовок заметки или 0 для выхода в главное меню: ")
            if noteHeader == "0":
                mainProg()
            else:
                noteContent = input("Введите тело заметки или 0 для выхода в главное меню: ")
                if noteContent == "0":
                    mainProg()
                else:
                    notes.append("id" + str(
                        idgeneration.newid()) + ';' + noteHeader + ';' + noteContent + ';' + str(current_datetime))
                    with open('notes.csv', 'a') as csvfile:
                        writer = csv.writer(csvfile, dialect='РАЗДЕЛИТЕЛЬ', skipinitialspace=True)
                        writer.writerow(("id" + str(idgeneration.newid()), noteHeader, noteContent, str(current_datetime)))
                    csvfile.close()
                    print("Заметка успешно сохранена")
                    print(notes)
                    mainProg()
        elif command == "2":
            while True:
                print("Введите текст для поиска или:\n"
                      "all - вывести все записи\n"
                      "0 - выйти в главное меню\n")
                TTS = input()
                if TTS == "0":
                    mainProg()
                elif TTS == "":
                    print("Вы ничего не ввели\n")
                elif TTS == "all":
                    with io.open('notes.csv', encoding='utf-8') as file:
                        for line in file:
                            print(line, end='')
                        file.close()
                else:
                    counter = 0
                    with io.open('notes.csv', encoding='utf-8') as file:
                        for line in file:
                            if TTS in line:
                                print(line, end='')
                                counter += 1
                        file.close()
                    if counter == 0:
                        print("Такой заметки нет\n")
                    file.close()
        # elif command == "3":


        elif command == "4":
            while True:
                print("Введите id заметки, которую нужно удалить:\n"
                      "0 - выйти в главное меню\n")
                idtodelete = input()
                counter = 0
                with io.open('notes.csv', encoding='utf-8') as file:
                    for line in file:
                        if idtodelete in line:
                            counter += 1
                    file.close()
                if counter == 0:
                    print("Такого id нет, попробуйте еще раз\n"
                          "\n")
                elif idtodelete.isdigit():
                    idsearchdelete(idtodelete)
                    print("Заметка с id "+idtodelete+" удалена\n")
                elif idtodelete == "0":
                    mainProg()
                else:
                    print("Неверный id, попробуйте еще раз")





        elif command == "5":
            exit()


mainProg()
