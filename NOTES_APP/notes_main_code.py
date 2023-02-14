import csv
import io
from datetime import datetime

from NOTES_APP.FUNCTIONS import idgeneration
from NOTES_APP.FUNCTIONS.findprintid import findid
from NOTES_APP.FUNCTIONS.idsearchedit import idsearchheader, idsearchbody
from NOTES_APP.FUNCTIONS.searchdeleteid import idsearchdelete
from NOTES_APP.FUNCTIONS.sortstrings import sortids

csv.register_dialect('РАЗДЕЛИТЕЛЬ', delimiter=';', skipinitialspace=True)
filecontent = []
notes = []
current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def mainMenu():
    print("1. Создать заметку\n"
          "2. Поиск по заметкам\n"
          "3. Редактировать заметку\n"
          "4. Удалить заметку\n"
          "5. Выход\n")


def mainProg():
    mainMenu()

    while True:
        command = str(input("Выберите команду: "))
        try:
            if int(command) < 1 or int(command) > 5:
                print("Неверная команда, только цифры от 1 до 5")
                mainProg()
        except ValueError:
            print("Неверная команда, только цифры от 1 до 5")
            mainProg()
        if command == "1":
            while True:
                noteHeader = input("Введите заголовок заметки или 0 для выхода в главное меню: ")
                if ";" in noteHeader:
                    print("Символ ; не допускается попробуйте еще раз")
                elif noteHeader == "0":
                    mainProg()
                else:
                    while True:
                        noteContent = input("Введите заметку или 0 для выхода в главное меню: ")
                        if ";" in noteContent:
                            print("Символ ; не допускается попробуйте еще раз")
                        elif noteContent == "0":
                            mainProg()
                        else:
                            notes.append(str(
                                idgeneration.newid()) + ';' + noteHeader + ';' + noteContent + ';' + str(
                                current_datetime))
                            with open('CSV/notes.csv', 'a', encoding="utf-8") as csvfile:
                                csvfile.write("\n" + str(
                                    idgeneration.newid()) + ";" +
                                              noteHeader + ";" +
                                              noteContent + ";" +
                                              str(current_datetime))
                                csvfile.close()
                            sortids()
                            print("Заметка успешно сохранена\n")
                            print((str(notes).split(";"))[0]
                                  + " | " + (str(notes).split(";"))[1]
                                  + " | " + (str(notes).split(";"))[2]
                                  + " | " + (str(notes).split(";"))[3]+"\n")
                            mainProg()
        elif command == "2":
            while True:
                print("\nВведите текст для поиска по всем заметкам или:\n"
                      "all - вывести все заметки\n"
                      "0 - вернуться в главное меню\n")
                texttosearchorcommand = input()
                if texttosearchorcommand == "0":
                    mainProg()
                elif texttosearchorcommand == "":
                    print("Вы ничего не ввели\n")
                elif texttosearchorcommand == "all":
                    with io.open('CSV/notes.csv', 'r', encoding='utf-8') as file:
                        if file.readlines() == []:
                            print("Заметок нет")
                            file.close()
                        else:
                            with io.open('CSV/notes.csv', 'r', encoding='utf-8') as file:
                                for line in file:
                                    print((line.split(";"))[0]
                                              + " | " + (line.split(";"))[1]
                                              + " | " + (line.split(";"))[2]
                                              + " | " + (line.split(";"))[3])
                                file.close()
                else:
                    counter = 0
                    with io.open('CSV/notes.csv', encoding='utf-8') as file:
                        for line in file:
                            if texttosearchorcommand in line:
                                print((line.split(";"))[0]
                                      + " | " + (line.split(";"))[1]
                                      + " | " + (line.split(";"))[2]
                                      + " | " + (line.split(";"))[3])
                                counter += 1
                        file.close()
                    if counter == 0:
                        print("Такой заметки нет или команда введена неверно")
                    file.close()
        elif command == "3":
            while True:
                print("Введите id заметки, которую нужно отредактировать:\n"
                      "0 - выйти в главное меню\n")
                idtoedit = input()
                if idtoedit == "0":
                    mainProg()
                counter = 0
                with io.open('CSV/notes.csv', encoding='utf-8') as file:
                    for line in file:
                        if idtoedit == line.split(';')[0]:
                            counter += 1
                    file.close()
                if counter == 0:
                    print("Такого id нет или он введен неправильно, попробуйте еще раз\n")
                elif idtoedit.isdigit() and idtoedit != 0:
                    print("Следующая заметка будет отредактирована:\n")
                    findid(idtoedit)
                    newheader = input("Введите новый заголовок или не"
                                        " вводите ничего, чтобы оставить без изменений: \n")
                    while ';' in newheader:
                        newheader = input("Символ ; недопустим, попробуйте еще раз: \n")
                    if newheader == "":
                        newheader = idsearchheader(idtoedit)
                    newbody = input("Введите новый текст заметки или не "
                                     " вводите ничего, чтобы оставить без изменений: \n")
                    while ';' in newbody:
                        newbody = input("Символ ; недопустим, попробуйте еще раз: \n")
                    if newbody == "":
                        newbody = idsearchbody(idtoedit)
                    idsearchdelete(idtoedit)
                    with open('CSV/notes.csv', 'a', encoding="utf-8") as csvfile:
                        csvfile.write("\n"
                                                      + idtoedit + ";"
                                                      + newheader + ";"
                                                      + newbody + ";"
                                                      + str(current_datetime) + "\n")
                        print("Заметка " + idtoedit
                                              + " | " + newheader
                                              + " | " + newbody
                                              + " | " + str(current_datetime)
                                              + " отредактирована")
                        csvfile.close()
                        sortids()
                        mainProg()
        elif command == "4":
            while True:
                print("Введите id заметки, которую нужно удалить:\n"
                      "0 - выйти в главное меню\n")
                idtodelete = input()
                if idtodelete == "0":
                    mainProg()
                counter = 0
                with io.open('CSV/notes.csv', encoding='utf-8') as file:
                    for line in file:
                        if idtodelete == line.split(';')[0]:
                            counter += 1
                    file.close()
                if counter == 0:
                    print("Такого id нет или id указан неправильно, попробуйте еще раз\n"
                          "\n")
                elif idtodelete.isdigit() and idtodelete != 0:
                    idsearchdelete(idtodelete)
                    print("Заметка с id " + idtodelete + " удалена\n")
        elif command == "5":
            exit()
