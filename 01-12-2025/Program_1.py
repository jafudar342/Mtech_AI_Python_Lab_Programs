l = [89, 78, 99, 67, 82]

total_marks = 0
for i in l:
    total_marks += i


def avg(total_marks):
    return total_marks / len(l)


print(f"Total marks = {total_marks}")
print(f"Average = {avg(total_marks)}")
