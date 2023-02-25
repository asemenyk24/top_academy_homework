try:
    number = int(input("Enter your number: "))
    print("Please choose degree of a number from 0 to 7.")
    degree = int(input("Enter degree 0-7: "))
    if degree < 0 or degree > 7:
        raise RuntimeError("Out of range!")
    else:
        result = number ** degree
        print(f"Your result is {result}!")
except ValueError:
    print("Operate integer numbers only!")
except RuntimeError as error:
    print(error)
