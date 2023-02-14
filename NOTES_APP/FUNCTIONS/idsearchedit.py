def idsearchheader(inputid):
    INFILE = './CSV/notes.csv'
    FIND = str(inputid) + ";"
    ENC = "utf-8"
    with open(INFILE, 'r', encoding=ENC) as infile:
        for line in infile:
            if FIND in line:
                return (line.split(";"))[1]

def idsearchbody(inputid):
    INFILE = './CSV/notes.csv'
    FIND = str(inputid) + ";"
    ENC = "utf-8"
    with open(INFILE, 'r', encoding=ENC) as infile:
        for line in infile:
            if FIND in line:
                return (line.split(";"))[2]
