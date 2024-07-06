def age():
    try:
        age = int(input("Please enter your age: "))
        
        if age < 0:
            print(" Please enter a valid age.")
        elif age < 18:
            print("You are a minor.")
        elif age < 65:
            print("You are an adult.")
        else:
            print("You are a senior.")
    except ValueError:
        print("Invalid input. Please enter a number.")
age()

