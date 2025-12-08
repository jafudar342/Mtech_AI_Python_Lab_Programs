num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp != 0:
    r = temp % 10
    reverse = reverse * 10 + r
    temp = temp // 10

if reverse == num:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
