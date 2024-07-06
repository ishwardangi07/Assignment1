a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))
choice=input('Enter an operator:')
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if(b!=0):
       return a/b
    else:
        return "Input Error."
if choice == "+":
    result = addition(a,b)
elif choice == "-":
    result = subtraction(a,b)
elif choice == "*":
    result = multiplication(a,b)
elif choice == "/":
    result = division(a,b)
else:
    result = "Invalid operator"

print(f"Result: {result}")


