a=int(input('enter a number:'))
if a>1:
    count=0
    for i in range(2,a):
        if a%i==0:
            count=count+1
    if count>=1:
        print('the number is not prime number')
    else:
        print('the number is prime number')
else:
    if a==0:
        print('zero is neither prime nor composite.')
    if a==1:
        print('1 is neither prime nor composite')



