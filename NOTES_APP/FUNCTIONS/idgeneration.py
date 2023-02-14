import io

filecontent = []

def newid():
    with io.open('./CSV/notes.csv', encoding='utf-8') as file:
        for line in file:
            filecontent.append(line)
    if filecontent == []:
        lastitemid = 1
        return lastitemid
    else:
        lastitem = filecontent[-1]
        lastitemid = int(lastitem.split(';')[0])
        file.close()
        return lastitemid+1




