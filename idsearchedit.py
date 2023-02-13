import csv
import io
import os


def idsearcheheader():

    inputid = 99
    INFILE = "notes.csv"
    FIND = str(inputid) + ";"
    OUTFILE = "new_notes.csv"
    ENC = "utf-8"
    with open(INFILE, 'r', encoding=ENC) as infile, open(OUTFILE, "w", encoding=ENC) as outfile:
        for line in infile:
            if FIND == line.split(';')[0]:
                print(line.split(";")[1])


idsearcheheader()

    #
    # infile.close()
    # outfile.close()
    #





    # with open(INFILE, 'w', encoding=ENC) as infile, open(OUTFILE, "r", encoding=ENC) as outfile:
    #     for line in outfile:
    #         infile.write(line)
    # infile.close()
    # outfile.close()

    # os.remove(OUTFILE)
