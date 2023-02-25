try:
    number = int(input("Pls enter your number from range 1-100: "))
    if number < 1 or number > 100:
        raise RuntimeError('Out of range!')
    if number % 3 == 0:
        print("Fizz!")
    elif number % 5 == 0:
        print("Buzz!")
    elif number % 15 == 0:
        print("Fizz Buzz!")
    else:
        print(f"{number}!")
except ValueError:
    print("Operate with integer numbers only!")
except RuntimeError as error:
    print(error)
