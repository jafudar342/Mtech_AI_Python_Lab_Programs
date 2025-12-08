num = int(input("Enter a number: "))
fact = 1
temp = num
while num >= 1:
    fact = fact * num
    num = num - 1
print(f"Factorial of {temp} is {fact}")
