words = {}
infile = open("AI.txt", "r")
word_file = infile.read()

for word in word_file.split():
    if word not in words:
        words[word] = 1
    elif word in words:
        words[word] += 1
print(words)

infile.close()
