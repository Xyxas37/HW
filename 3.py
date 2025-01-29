def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")

choice = input("Введите номер операции (1 или 2): ")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if choice == '1':
    result = add(num1, num2)
    print(f"Результат сложения: {result}")
elif choice == '2':
    result = subtract(num1, num2)
    print(f"Результат вычитания: {result}")
else:
    print("Неверный выбор. Пожалуйста, выберите 1 или 2.")