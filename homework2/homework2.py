while True:
    try:
        a = int(input("введите первое целое число: "))
        a2 = int(input("введите второе целое число: "))
        summa = a + a2
        print("сумма равна", summa)
    except ValueError:
        print("пожалуйста, введите корректные целые числа.")
