from math import factorial

n = 5

for i in range(n):
    print(" " * (n - i), end="")

    for j in range(i+1):
        value = factorial(i) // (factorial(j) * factorial(i-j))
        print(value, end=" ")
    print()  # for next line
