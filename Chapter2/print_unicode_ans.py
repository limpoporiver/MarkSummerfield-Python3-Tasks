#!/usr/bin/env python3
import sys
import unicodedata

words = []


if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage:{0} [string1 string2 ... stringN]".format(sys.argv[0]))
        words = None
    else:
        for word in sys.argv[1:]:
            words.append(word.lower())


def print_unicode_table(words):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if set(words).issubset(set(name.lower().split())):
            try:
                print("{0:7}  {0:5X}  {0:^3c}  {1}".format(code, name.title()))
            except UnicodeEncodeError:
                print("missed because \"utf-8\" codec can't encode surrogates")
        code += 1


if words is not None:
    print_unicode_table(words)