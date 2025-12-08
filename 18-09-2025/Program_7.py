a, b, c = map(int, input("enter a number: ").split())
if a > b and a > c:
    print(f"{a} is bigger")
elif b > a and b > c:
    print(f"{b} is bigger")
else:
    print(f"{c} is bigger")
