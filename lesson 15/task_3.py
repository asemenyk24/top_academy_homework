operators = {
    1: "megafon > tele2",
    2: "megafon > mts",
    3: "tele2 > megafon",
    4: "tele2 > mts",
    5: "mts > tele2",
    6: "mts > megafon"
}
taxes = {
    1: 1.337,
    2: 1.448,
    3: 1.69,
    4: 2.28,
    5: 1.300,
    6: 1.337
}
try:
    price = float(input("Enter price of your call: "))
    if price <= 0:
        raise RuntimeError("You can't call for free!")
    print("Choose available option:")
    for key in operators:
        print(f"{key} - {operators[key]}.")
    users_choice = int(input("Enter option's number (integer number only): "))
    if users_choice > 6 or users_choice < 1:
        raise RuntimeError("Choose AVAILABLE option!")
    result = taxes[users_choice] * price
    print(f"Price of your call is {result} rubles!")
except ValueError:
    print("Operate with suitable numbers!")
except RuntimeError as error:
    print(error)
