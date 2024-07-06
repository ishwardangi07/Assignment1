num1=int(input('enter a first number:'))

num2=int(input('enter a second number:'))

try:
    first_div=num1/num2
    print(f"{num1} divided by {num2} is {first_div}")
except ZeroDivisionError:
    print('you can not divide by zero')

