"""
Code should:
- Open a file
- count how many times a space-separated word occurs in the file
- print that count to the screen
"""

text_file = open('twain.txt')

word_count = {}

# combine all line lists into one long list .extend/.append
for line in text_file:
    words = line.split()

    for word in words:
        # remove punctuation at end of word, allowing for words that are 
        while not word[-1].isalpha() and not word[-1].isdigit() and len(word) > 1:
            word = word[:-1]

        while not word[0].isalpha() and not word[0].isdigit() and len(word) > 1:
            word = word[1:]
        # increment word count by 1
        word_count[word] = word_count.get(word, 0) + 1

# print words in alphabetical order
for key, value in sorted(word_count.iteritems())[:100]:
    print "{}: {:,}".format(key, value)