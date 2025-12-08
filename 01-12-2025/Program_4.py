class Numbers:
    def __init__(self, list):
        self.list = list

    def largest(self):
        max = self.list[0]
        for num in self.list:
            if num > max:
                max = num
        return max


l = [5, 6, 8, 9, 10, 88, 9]

obj = Numbers(l)
max = obj.largest()
print("Maximum = ", max)
