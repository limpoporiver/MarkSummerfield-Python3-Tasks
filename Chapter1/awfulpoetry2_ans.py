#!/usr/bin/env python3

from random import randint, choice
import sys


articles = ["the", "a", "her", "his", "another"]
nouns = ["cat", "dog", "hamster", "woman", "superman", "cheburashka", "levtolstoi", "rocketman"]
verbs = ["sang", "jumped", "ran", "sleeped", "ate", "hated"]
adverbs = ["loudly", "quietly", "well", "badly"]

sentence = [[articles, nouns, verbs, adverbs], [articles, nouns, verbs]]

poem_strings = 5
if len(sys.argv) > 1:
    try:
        if 1 <=int(sys.argv[1]) <= 10:
            poem_strings = int(sys.argv[1])
        else:
            print("Only 1 - 10 strings allowed (5 by default): ")
    except ValueError as err:
        print(err, "We use 5 strings by default")

while poem_strings > 0:
    poem_string = ""
    word = 0
    #due to task I need to use randint to choose type of sentence
    sentence_choice = randint(0, len(sentence) - 1)
    while word < len(sentence[sentence_choice]):
        poem_string += f"{choice(sentence[sentence_choice][word])} "
        word += 1
    poem_strings -= 1
    print(poem_string)
