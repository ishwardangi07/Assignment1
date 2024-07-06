def factorial(n):
    factorial=1
    if n==0&1:
        return 1
    else:
        for i in range(1,n+1):
            factorial=factorial*i
    return factorial
n=int(input('enter a number:'))
fact=factorial(n)
print(f"the factorial of {n} is {fact}")
