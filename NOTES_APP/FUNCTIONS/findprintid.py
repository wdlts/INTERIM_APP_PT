def findid(inputid):
    INFILE = './CSV/notes.csv'
    FIND = str(inputid)
    ENC = "utf-8"
    with open(INFILE, 'r', encoding=ENC) as infile:
        for line in infile:
            if FIND == line.split(";")[0]:
                print((line.split(";"))[0]
                      + " | " + (line.split(";"))[1]
                      + " | " + (line.split(";"))[2]
                      + " | " + (line.split(";"))[3])