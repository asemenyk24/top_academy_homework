from itertools import product

digits = [str(i) for i in range(1, 10)]
signs = ('', '+', '-')

# Работаю с декартовыми произведениями, получаю возможные комбинации.
combos = [a + b for (a, b) in product(digits[:-1], signs)]
# Группирую каждую цифру с 3-мя возможными вариантами знаков.
combos = [combos[i:i + 3] for i in range(0, len(combos), 3)]
# Цепляю 9, после которой не может быть знака.
combos += [[digits[-1]]]


def search_all_hundreds(number):
    expressions = []
# Вновь работаю с декартовым произведением, выводя все возможные варианты знаков в последовательности.
    for j in product(*combos):
        expression = "".join(j)
        if eval(expression) == number:
            expressions.append(expression)

    print(f"You have {len(expressions)} possible variants of getting 100.")
    print("Here's available expressions:")
    for variant in expressions:
        print(f"\t{variant}")


search_all_hundreds(100)
