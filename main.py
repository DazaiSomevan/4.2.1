from utils import factorial, fibonacci

def main():
    number = input("Введіть число:")
    result = factorial(number)
    result1 = fibonacci(number)
    print(f"Факторіал числа {number} дорівнює {result}")
    print(f"{number}-те число Фібоначчі дорівнює {result1}")

if name == "__main__":
    main()
