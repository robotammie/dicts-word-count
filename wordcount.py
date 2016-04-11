"""
Code should:
- Open a file
- count how many times a space-separated word occurs in the file
- print that count to the screen
"""

text_file = open('test.txt')

for line in text_file:
    line = line.rstrip()
    word = line.split(' ')

    print word
