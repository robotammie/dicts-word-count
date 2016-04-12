"""
Code should:
- Open a file
- count how many times a space-separated word occurs in the file
- print that count to the screen
"""

import sys
import string
import re

text_file = open(sys.argv[1])

word_count = {}

# combine all line lists into one long list .extend/.append
all_words = []

# open file, add all words in file to all_words
for line in text_file:
    words = re.split('[(--)\s]',line)

    all_words.extend(words)

# count appearances of each word
for word in all_words:

    #removes all punctuation from beginnings and ends of words
    word = word.strip(string.punctuation)

    # increment word count by 1
    word_count[word] = word_count.get(word, 0) + 1

# print words in alphabetical order
for key, value in word_count.iteritems():
    print "{}: {:,}".format(key, value)
