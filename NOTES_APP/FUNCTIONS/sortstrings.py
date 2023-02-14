from natsort import natsorted


def sortids():
    inFile = open('./CSV/notes.csv', "r", encoding='utf-8')
    reader = inFile.readlines()
    scs = []
    for i in reader:
        if i != '\n':
            scs.append(i)
    outputsorted = (natsorted(scs, key=lambda line: line.split(';')[0]))
    inFile = open('./CSV/notes.csv', "w", encoding='utf-8')
    for line in outputsorted:
         inFile.write(line)
    inFile.close()

