class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        #self.total = None

    def add(self):
        self.total = self.num1 + self.num2
        return self.total

    def sub(self):
        self.total = self.num1 - self.num2
        return self.total

    def mul(self):
        self.total = self.num1 * self.num2
        return self.total

    def div(self):
        if self.num2 == 0:
            print("Cannot divided by 0! ")
            return None
        else:
            self.total = self.num1 / self.num2
            return self.total


num1_input = (int(input("Enter a first number:  ")))
num2_input = (int(input("Enter a second number:  ")))
calculator= Calculator(num1_input, num2_input)

operation = input("Enter the operation you want! \n + for Addition\n - for Subtraction \n * for Multiplication \n / for divide:\n ")
if operation == "+":
    result = calculator.add()

elif operation == "-":
    result = calculator.sub()

elif operation == "*":
    result = calculator.mul()
elif operation == "/":
    result = calculator.div()
else:
    print("Enter a valid function!  ")
if result is not None:
    print(f"{calculator.num1} {operation} {calculator.num2} is {calculator.total}")




