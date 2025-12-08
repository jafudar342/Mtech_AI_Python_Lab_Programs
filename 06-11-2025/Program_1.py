num = int(input("Enter a number: "))
count = 0

for i in range(1, num+1):
    if num == 1:
        print("Number is coprime")
        break
    if num % i == 0:
        count = count + 1
if count == 2:
    print("Number is prime ")
else:
    print("Number is not prime")
