def find_maximum(numbers):
    if not numbers:
        return "The list is empty."
    
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value

input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, input.split()))

max_value = find_maximum(numbers)
print("The maximum value in the list is:", max_value)

