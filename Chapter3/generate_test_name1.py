#!/usr/bin/env python3

from random import choice

def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "data/forenames.txt"), 
                            (surnames, "data/surnames.txt")):
        for name in open(filename, encoding="utf-8"):
            names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
fh = open("test-names1.txt", "w", encoding="utf-8")
for i in range(100):
    line = "{0} {1}\n".format(choice(forenames),
                               choice(surnames))
    fh.write(line)
