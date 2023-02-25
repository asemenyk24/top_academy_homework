while True:
    try:
        your_numbers = input('Enter 3 integer numbers divided by space, ex: "2 4 1" :').split()
        numbers = list(map(int, your_numbers))
        print(f"Your numbers are: {numbers}")
    except ValueError:
        print("Pls operate with integer numbers only!")
        continue
    print('Enter one of the valid commands: "m" - max, "l" - least, "a" - average, "q" - exit!')
    action = input("Enter your command: ")
    if action == "m":
        result = max(numbers)
        print(f"The highest numbers is {result}!")
    elif action == "l":
        result = min(numbers)
        print(f"Least number is {result}!")
    elif action == "a":
        result = int(sum(numbers)/len(numbers))
        print(f"Average of numbers is {result}!")
    elif action == "q":
        print("Bye!")
        break
    else:
        print("Use valid commands only! Try again!")
        continue