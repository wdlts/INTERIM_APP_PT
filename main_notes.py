import csv
import time
from datetime import datetime
import io
import idgeneration
from findprintid import findid
from searchdeleteid import idsearchdelete
from sortstrings import sortids

csv.register_dialect('РАЗДЕЛИТЕЛЬ', delimiter=';', skipinitialspace=True)
filecontent = []
notes = []
current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
myFile = open('notes.csv', 'a', encoding='utf-8')


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
            while True:
                noteHeader = input("Введите заголовок заметки или 0 для выхода в главное меню: ")
                if ";" in noteHeader:
                    print("Символ ; не допускается попробуйте еще раз")
                elif noteHeader == "0":
                    mainProg()
                else:
                    while True:
                        noteContent = input("Введите тело заметки или 0 для выхода в главное меню: ")
                        if ";" in noteContent:
                            print("Символ ; не допускается попробуйте еще раз")
                        elif noteContent == "0":
                            mainProg()
                        else:
                            notes.append(str(
                                idgeneration.newid()) + ';' + noteHeader + ';' + noteContent + ';' + str(current_datetime))
                            with open('notes.csv', 'a', encoding="utf-8") as csvfile:
                                csvfile.write("\n" + str(
                                    idgeneration.newid()) + ";" +
                                              noteHeader + ";" +
                                              noteContent + ";" +
                                              str(current_datetime))
                                csvfile.close()
                            sortids()

                            print("Заметка успешно сохранена")
                            print(notes)
                            mainProg()
        elif command == "2":
            while True:
                print("\nВведите текст для поиска по всем заметкам или:\n"
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

        elif command == "3":
            while True:
                print("Введите id заметки, которую нужно отредактировать:\n"
                      "0 - выйти в главное меню\n")
                idtoedit = input()
                if idtoedit == "0":
                    mainProg()

                counter = 0
                with io.open('notes.csv', encoding='utf-8') as file:
                    for line in file:
                        if idtoedit == line.split(';')[0]:
                            counter += 1
                    file.close()
                if counter == 0:
                    print("Такого id нет или он введен направильно, попробуйте еще раз\n")

                elif idtoedit.isdigit() and idtoedit != 0:
                    print("Следующая заметка будет отредактирована:\n")
                    findid(idtoedit)
                    newheader = input("Введите новый заголовок: \n")
                    newbody = input("Введите новый текст заметки: \n")
                    idsearchdelete(idtoedit)
                    with open('notes.csv', 'a', encoding="utf-8") as csvfile:
                        csvfile.write("\n"+idtoedit + ";" + newheader + ";" + newbody + ";" + str(current_datetime)+"\n")
                        print("Заметка " + idtoedit + " ## " + newheader + " ## " + newbody + " ## " + str(
                            current_datetime) + " отредактирована")
                    csvfile.close()
                    sortids()

        elif command == "4":
            while True:
                print("Введите id заметки, которую нужно удалить:\n"
                      "0 - выйти в главное меню\n")
                idtodelete = input()
                if idtodelete == "*":
                    mainProg()

                counter = 0
                with io.open('notes.csv', encoding='utf-8') as file:
                    for line in file:
                        if idtodelete == line.split(';')[0]:
                            counter += 1
                    file.close()
                if counter == 0:
                    print("Такого id нет или id неверный, попробуйте еще раз\n"
                          "\n")
                elif idtodelete.isdigit() and idtodelete != 0:
                    idsearchdelete(idtodelete)
                    print("Заметка с id " + idtodelete + " удалена\n")

        elif command == "5":
            exit()
