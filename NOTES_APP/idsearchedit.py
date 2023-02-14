def idsearchheader(inputid):
    INFILE = "notes.csv"
    FIND = str(inputid) + ";"
    ENC = "utf-8"
    with open(INFILE, 'r', encoding=ENC) as infile:
        for line in infile:
            if FIND in line:
                return (line.split(";"))[1]

def idsearchbody(inputid):
    INFILE = "notes.csv"
    FIND = str(inputid) + ";"
    ENC = "utf-8"
    with open(INFILE, 'r', encoding=ENC) as infile:
        for line in infile:
            if FIND in line:
                return (line.split(";"))[2]




    # with open(INFILE, 'w', encoding=ENC) as infile, open(OUTFILE, "r", encoding=ENC) as outfile:
    #     for line in outfile:
    #         infile.write(line)
    # infile.close()
    # outfile.close()

    # os.remove(OUTFILE)
