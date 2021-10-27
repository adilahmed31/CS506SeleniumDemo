import requests

class CalculatorError(Exception):
    pass

class Calculator(object):

    def add(self,x,y):
        try:
            return x+y
        except TypeError:
            raise CalculatorError("Type Error")
        except ValueError:
            raise CalculatorError("Value Error")

    def subtract(self,x,y):
        return x-y

    def divide(self,x,y):
        if y==0:
            raise CalculatorError("ZeroDivisionError")
        return x/y
 
    def getVersion(self,year):
        output = requests.get(f'http://cs.wisc.edu/{year}')
        if output.ok:
            return output.text
        else:
            return "Bad Response"