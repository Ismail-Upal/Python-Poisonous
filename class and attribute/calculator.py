class Calculator:
    brand = 'Casio MS993'

    def add(self, *args):
        return sum(args)
    
    def deduct(self, *args):
        res = args[0]
        for i in args[1:]:
            res-=i
        return res
    
    def multiply(self, *args):
        res=args[0]
        for i in args[1:]:
            res*=i
        return res
    
    def divide(self, *args):
        res=args[0]
        for i in args[1:]:
            if i!=0:
                res/=i
        return res
        
    
calc = Calculator()
print(calc.add(4,3,2))
print(calc.deduct(2,3,2,6))
print(calc.multiply(2,3,3,5,3))
print(calc.divide(2,3,3,4))