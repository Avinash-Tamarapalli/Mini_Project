class Calculator():
    result = 0

    def EnterNumber(self,num):
        self.num = num

    def Add(self):
        self.add = Calculator.result + self.num
        Calculator.result = self.add

    def subtract(self):
        self.subtract = Calculator.result - self.num
        Calculator.result = self.subtract

    def multiply(self):
        self.multiply = Calculator.result * self.num
        Calculator.result = self.multiply

    def divide(self):
        try :
            self.divide = Calculator.result // self.num
        except ZeroDivisionError:
            Calculator.result = "Can't be divide by 0"

    def print_result(self):
        self.result = Calculator.result 
        print(self.result)
    


Calc = Calculator()

Calc.EnterNumber(3) # after every EnterNumber call, some operation should be called
Calc.Add()

Calc.EnterNumber(5)
Calc.subtract()

Calc.EnterNumber(2)
Calc.multiply()

Calc.EnterNumber(0)
Calc.divide()

Calc.print_result()