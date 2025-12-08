l = [1, 2, 3, 4, 5]

i, j = 0, len(l) - 1

while i < j:
    l[i], l[j] = l[j], l[i]
    i = i + 1
    j = j - 1

print(l)
