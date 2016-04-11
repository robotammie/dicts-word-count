"""
Code should:
- Open a file
- count how many times a space-separated word occurs in the file
- print that count to the screen
"""

text_file = open('twain.txt')

word_count = {}

for line in text_file:
    line = line.rstrip()

    words = line.split()

    # use method to make shorter
    for word in words:
        if word_count.get(word) != None:
            word_count[word] += word_count[word]
        else:
            word_count[word] = 1

for key, value in word_count.iteritems():
    print "%s: %d" % (key, value)