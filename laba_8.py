class H1(BaseException):
    pass

class H2(BaseException):
    pass

class H3(BaseException):
    pass

class Ashan_Class:
    def method1(self, argument):
        if argument < 0:
            raise H1("Argument should be non-negative")
        elif argument == 0:
            raise H2("Argument should be non-zero")
        else:
            return argument ** 2

    def method2(self, argument1, argument2):
        if argument1 == argument2:
            raise H3("Arguments should be different")
        else:
            return argument1 + argument2

    def method3(self, argument):
        if not isinstance(argument, str):
            raise TypeError("Argument should be a string")
        elif len(argument) < 5:
            raise ValueError("String should be at least 5 characters long")
        else:
            return argument.upper()
        
class Processing:
    def __init__(self, obj):
        self.obj = obj

    def fix_method1(self, argument):
        try:
            result = self.obj.method1(argument)
        except H1 as x:
            print("Error:", x)
            result = None
        except H2 as x:
            print("Error:", x)
            result = None
        return result

    def fix_method2(self, argument1, argument2):
        try:
            result = self.obj.method2(argument1, argument2)
        except H3 as x:
            print("Error:", x)
            result = None
        return result

    def fix_method3(self, argument):
        try:
            result = self.obj.method3(argument)
        except TypeError as x:
            print("Error:", x)
            result = None
        except ValueError as x:
            print("Error:", x)
            result = None
        return result
    
obj = Ashan_Class()
proc = Processing(obj)

print(proc.proc_method1(2))
print(proc.proc_method1(-1))

print(proc.proc_method2(2, 3))
print(proc.proc_method2(2, 2))

print(proc.proc_method3("hello"))
print(proc.proc_method3(123))

print(proc.proc_method3("hi"))