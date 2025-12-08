class MathOps:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n-1)


obj = MathOps()
num = int(input("Enter a number: "))

result = obj.factorial(num)
print("Factorial of ", num, "is", result)
