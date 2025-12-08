class Pattern:
    def square(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()

    def triangle(self, n):
        for i in range(1, n+1):
            for j in range(i):
                print("*", end=" ")
            print()


obj = Pattern()
num = int(input("Enter size: "))

print("Square Pattern: ")
obj.square(num)

print("Triangle Pattern: ")
obj.triangle(num)
