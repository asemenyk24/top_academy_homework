while True:
    try:
        meters = int(input("Pls enter meters by integer number: "))
        print(f"You entered {meters} m.")
    except ValueError:
        print("It only works with integer numbers!")
        continue
    print("Use commands: 'mm' - meters to miles, 'mi' meters to inches, 'my' - yards, 'q' - exit.")
    action = input("Pls enter command to continue!")
    if action == "mm":
        result = round((meters * 0.000621371), 5)
        print(f"It's equal to {result} miles!")
    elif action == "mi":
        result = round((meters * 39.3701), 5)
        print(f"It's equal to {result} inches!")
    elif action == "my":
        result = round((meters * 1.09361), 5)
        print(f"It's equal to {result} yards!")
    elif action == "q":
        print("Bye!")
        break
    else:
        print("Use valid commands only!")
        continue
        