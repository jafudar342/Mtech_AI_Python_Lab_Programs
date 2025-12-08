l = [2, 3, 1, 4, 8, 5, 10]
max = l[0]
for i in l:
    if max < i:
        max = i
print(f"Largest number in list is {max}")
