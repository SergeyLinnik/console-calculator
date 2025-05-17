def calculator():
    print("Консольный калькулятор")
    print("----------------------")
    
    # Сложение
    try:
        num1 = float(input("Введите первое число для сложения: "))
        num2 = float(input("Введите второе число для сложения: "))
        print(f"Результат: {num1 + num2}\n")
    except ValueError:
        print("Ошибка: введите числа!\n")
    
    # Вычитание
    try:
        num1 = float(input("Введите первое число для вычитания: "))
        num2 = float(input("Введите второе число для вычитания: "))
        print(f"Результат: {num1 - num2}\n")
    except ValueError:
        print("Ошибка: введите числа!\n")
    
    # Умножение
    try:
        num1 = float(input("Введите первое число для умножения: "))
        num2 = float(input("Введите второе число для умножения: "))
        print(f"Результат: {num1 * num2}\n")
    except ValueError:
        print("Ошибка: введите числа!\n")
    
    # Деление
    try:
        num1 = float(input("Введите первое число для деления: "))
        num2 = float(input("Введите второе число для деления: "))
        if num2 == 0:
            print("Ошибка: деление на ноль!\n")
        else:
            print(f"Результат: {num1 / num2}\n")
    except ValueError:
        print("Ошибка: введите числа!\n")

if __name__ == "__main__":
    calculator()
