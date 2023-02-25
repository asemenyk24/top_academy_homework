import random


def generate_number():
    nums = [i for i in range(10)]
    number = []
    for j in range(4):
        digit = nums.pop(random.choice(range(len(nums))))
        number.append(str(digit))
    return number


number_to_guess = generate_number()


def bulls_and_cows(number, attempt):
    cows = 0
    bulls = 0
    user_attempt = list(input("Enter 4-digit number with no-repeats: "))
    print(user_attempt)
    for i in range(len(number)):
        if user_attempt[i] == number[i]:
            cows += 1
        if user_attempt[i] in number:
            bulls += 1
    if cows == 4:
        print(f"You've guessed the number {''.join(map(str,number))}. You used {attempt} attempts!")
    elif cows != 4:
        print(f"You have {bulls} bulls and {cows} cows, current attempt {attempt}. Keep trying!")
        bulls_and_cows(number, attempt + 1)


bulls_and_cows(number_to_guess, 1)
