import csv
import io
import os


def idsearchdelete(inputid):

    INFILE = "notes.csv"
    FIND = "id" + str(inputid) + ";"
    OUTFILE = "new_notes.csv"
    ENC = "utf-8"
    with open(INFILE, 'r', encoding=ENC) as infile, open(OUTFILE, "w", encoding=ENC) as outfile:
        for line in infile:
            if FIND not in line:
                outfile.write(line)
    infile.close()
    outfile.close()

    with open(INFILE, 'w', encoding=ENC) as infile, open(OUTFILE, "r", encoding=ENC) as outfile:
        for line in outfile:
            infile.write(line)
    infile.close()
    outfile.close()

    os.remove(OUTFILE)
