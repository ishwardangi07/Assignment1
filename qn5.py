def fibonacci_series(n):
    a, b = 0, 1
    series = []
    
    for _ in range(10):
        series.append(a)
        a, b = b, a + b
    
    return series
fib_series = fibonacci_series(10)
print("Fibonacci series:", fib_series)
