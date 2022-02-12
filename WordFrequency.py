words_dict = {}
infile = open("AI.txt", "r")
word_file = infile.read()

for word in word_file.split():
    if word not in words_dict:
        words_dict[word] = 1
    elif word in words_dict:
        words_dict[word] += 1
print(words_dict)

infile.close()
