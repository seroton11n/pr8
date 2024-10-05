summa=0
while True:
    user_input = input("введите число или 'stop'/'end' для завершения ввода: ")
    if user_input.lower() in ["stop", "end"]:
        break
    user_input = user_input.replace(',', '.')
    try:
        a = float(user_input)
        summa += a  
    except ValueError:
        print("ошибка: пожалуйста, введите корректное число.")
print(f"сумма введённых чисел: {summa}")
