file = open("file.txt", "r")
text = file.read().lower()

words = text.split()

freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

file.close()

print("Word frequency: ")
for word, count in freq.items():
    print(word, ":", count)
