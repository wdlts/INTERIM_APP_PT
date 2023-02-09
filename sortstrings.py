import io

FileName = ("temp.csv")
inFile = open('temp.csv', "r", encoding='utf-8')
outFile = open("output.txt", "w", encoding="utf8")
reader = inFile.readlines()
scs = []
for i in reader:
    scs.append(i)
    scs.sort()
for line in scs:
    outFile.write(line)



