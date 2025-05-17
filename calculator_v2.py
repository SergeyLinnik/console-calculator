def calculate():
    print("Улучшенный консольный калькулятор")
    print("---------------------------------")
    
    try:
        # Ввод данных
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Выберите операцию (+, -, *, /): ").strip()
        
        # Вычисление
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно!")
            result = num1 / num2
        else:
            raise ValueError("Недопустимая операция!")
        
        # Вывод результата
        print(f"\nРезультат: {num1} {operation} {num2} = {result:.2f}")
    
    except ValueError as e:
        print(f"\nОшибка: {e}")
    except ZeroDivisionError as e:
        print(f"\nОшибка: {e}")
    except Exception as e:
        print(f"\nНеожиданная ошибка: {e}")
    finally:
        print("\nРабота калькулятора завершена")

if __name__ == "__main__":
    calculate()
