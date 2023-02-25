while True:
    try:
        f_num = int(input("Enter first number: "))
        s_num = int(input("Enter second number: "))
        t_num = int(input("Enter third number: "))
        print(f"Your numbers are: {f_num}, {s_num}, {t_num}.")
    except ValueError:
        print("Enter integer numbers only!!!")
        continue
    print("Use one of the command to operate: 'q' - exit, 's' - sum, 'm' - multiply.")
    action = input("Your command is: ")
    if action == "s":
        result = f_num + s_num + t_num
        print(f"Sum of numbers is {result}!")
    elif action == "m":
        result = f_num * s_num * t_num
        print(f"Multiplication result is {result}!")
    elif action == "q":
        print("Bye!")
        break
    else:
        print("Pls operate with valid commands only!")
        continue