def get_float_input(prompt):
    while True:
        user_input = input(prompt).replace(',', '.')
        try:
            return float(user_input)
        except ValueError:
            print("ошибка: пожалуйста, введите корректное число.")
a = get_float_input("введите первое число: ")
b = get_float_input("введите второе число: ")

start = int(min(a, b))  
end = int(max(a, b))

integer = [i for i in range(start + 1, end)]

if integer:
    print(f"Целые числа между {a} и {b}:")
    for i in integer:
        print(i)
else:
    print(f"Нет целых чисел между {a} и {b}.")
