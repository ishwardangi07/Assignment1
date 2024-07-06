def function(a):
    if a == 0:
        return "0"
    binary_number = ""
    while a > 0:
        remainder = a % 2
        binary_number = str(remainder) + binary_number
        a = a // 2
    return binary_number
a = int(input("Enter a decimal number: "))
binary_number = function(a)
print(f"The binary equivalent of {a} is {binary_number}")