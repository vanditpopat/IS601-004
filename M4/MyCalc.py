class MyCalc:
    def _init_(self):
        self.ans = 0
    # vp645 02/27/2023 Creating a new instance to set the ans property zero.

    def add(self, num1, num2):
        self.ans = num1 + num2
        return self.ans
    # vp645 02/27/2023 Accept 2 equation and add it and then return the answer
    
    def subtract(self, num1, num2):
        self.ans = num1 - num2
        return self.ans
    #  vp645 02/27/2023 Accept 2 equation and subtract it to return the answer
    
    def multiply(self, num1, num2):
        self.ans = num1 * num2
        return self.ans
    #  vp645 02/27/2023 Accept 2 equation and multiply it and then return the answer
    
    def divide(self, num1, num2):
        try:
            result = float(num1) / float(num2)
            return result
        except ZeroDivisionError:
            return "Zero cannot be divided"
        except ValueError:
            return "Invalid input."
    #  vp645 02/27/2023 Accept 2 equation and divide it and then return the answer, we also check for exceptions if
    #  we divide the value by 0 and also if the equation is not converted to float

def main():
    calc = MyCalc()

    while True:
        try:
            equation = input("Enter your operation: ")
        except EOFError:
            print("Good Bye")
            break

        if equation.lower() == "quit":
            print("Good Bye")
            break

        nums = equation.split()
        if len(nums) != 3:
            print("Invalid input.")
            continue

        if nums[0] == "ans":
            num1 = calc.ans
        else:
            try:
                num1 = float(nums[0])
            except ValueError:
                print("Invalid input.")

        if nums[2] == "ans":
            num1 = calc.ans
        else:
            try:
                num2 = float(nums[2])
            except ValueError:
                print("Invalid input.")

        operator = nums[1]
        if operator == "+":
            result = calc.add(num1, num2)
        elif operator == "-":
            result = calc.subtract(num1, num2)
        elif operator == "*":
            result = calc.multiply(num1, num2)
        elif operator == "/":
            result = calc.divide(num1, num2)
            if result == "Zero cannot be divided":
                print(result)
                continue

        print(result)
        calc.ans = result if result != "Zero cannot be divided" else calc.ans

if __name__ == "__main__":
    main()