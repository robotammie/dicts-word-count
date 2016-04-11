"""
Code should:
- Open a file
- count how many times a space-separated word occurs in the file
- print that count to the screen
"""

text_file = open('test.txt')

word_count = {}

for line in text_file:
    line = line.rstrip()

    words = line.split()

    for word in words:
        if word in word_count:
            word_count[word] += word_count[word]
        else:
            word_count[word] = 1

print word_count
