import os


def idsearchdelete(inputid):

    INFILE = './CSV/notes.csv'
    FIND = inputid
    OUTFILE = './CSV/new_notes.csv'
    ENC = "utf-8"
    with open(INFILE, 'r', encoding=ENC) as infile, open(OUTFILE, "w", encoding=ENC) as outfile:
        for line in infile:
            if FIND != line.split(';')[0]:
                outfile.write(line)
    infile.close()
    outfile.close()

    with open(INFILE, 'w', encoding=ENC) as infile, open(OUTFILE, "r", encoding=ENC) as outfile:
        for line in outfile:
            infile.write(line)
    infile.close()
    outfile.close()

    os.remove(OUTFILE)
