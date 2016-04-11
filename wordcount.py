"""
Code should:
- Open a file
- count how many times a space-separated word occurs in the file
- print that count to the screen
"""

import sys

text_file = open(sys.argv[1])

word_count = {}

# combine all line lists into one long list .extend/.append
all_words = []

# open file, add all words in file to all_words
for line in text_file:
    words = line.split()
    all_words.extend(words)

# count appearances of each word
for word in all_words:
    # remove punctuation at end of word, allowing for words that are numbers
    while not word[-1].isalpha() and not word[-1].isdigit() and len(word) > 1:
        word = word[:-1]

    while not word[0].isalpha() and not word[0].isdigit() and len(word) > 1:
        word = word[1:]
    # increment word count by 1
    word_count[word] = word_count.get(word, 0) + 1

# print words in alphabetical order
for key, value in word_count.iteritems():
    print "{}: {:,}".format(key, value)
