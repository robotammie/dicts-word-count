"""
Code should:
- Open a file
- count how many times a space-separated word occurs in the file
- print that count to the screen
"""

text_file = open('test.txt')

word_count = {}

for line in text_file:
    # line = line.rstrip()
    words = line.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

for key, value in word_count.iteritems():
    print "%s: %d" % (key, value)