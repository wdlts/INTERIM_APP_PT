import csv
import io
import os


def idsearchdelete(inputid):
    # f = open('notes.csv', 'w')
    # for line in f:
    #     if "id" + str(inputid) + ";" not in line:
    #         with io.open('new_notes.csv', 'a') as file1:
    #             file1.writelines(line)
    # f.close()
    # file1.close()
    # os.remove('notes.csv')
    # os.rename('new_notes.csv', 'notes.csv')

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
