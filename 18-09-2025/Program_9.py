num = int(input("Enter a number: "))
sum = 0
i = 1
while i <= num:
    print(f"{i}", end=',')
    sum = sum + i
    i = i + 1
print(f"\nSum of first {num} natural numbers: {sum}")
