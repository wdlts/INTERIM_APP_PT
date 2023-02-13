from natsort import natsorted, ns


def sortids():
    inFile = open('notes.csv', "r", encoding='utf-8')
    # outFile = open("notes_temp.txt", "w", encoding="utf8")
    reader = inFile.readlines()
    scs = []
    for i in reader:
        if i != '\n':
            scs.append(i)
    outputsorted = (natsorted(scs, key=lambda line: line.split(';')[0]))
    inFile = open('notes.csv', "w", encoding='utf-8')
    for line in outputsorted:
         inFile.write(line)
    inFile.close()

