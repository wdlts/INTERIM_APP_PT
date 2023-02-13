import io

filecontent = []

def newid():
    with io.open('notes.csv', encoding='utf-8') as file:
        for line in file:
            filecontent.append(line)
    lastitem = filecontent[-1]
    lastitemid = int(lastitem.split(';')[0])
    file.close()
    return lastitemid+1




