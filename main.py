# Простой калькулятор
# Ввод данных

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operator = input("Введите операцию (+, -, *, /): ")

# Работа с операциями
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Деление на ноль невозможно!")
    else:
        result = num1 / num2
else:
    print("Неизвестная операция.")
    # Вывод данных
if operator in ('+', '-', '*', '/'):
    print("Результат:", result)






