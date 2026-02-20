from utils import factorial, fibonacci, find_gcd

def main():
    number = input("Введіть число:")
    number2 = input("Введіть число2:")
    result = factorial(number)
    result2 = find_gcd(number, number2)
    result1 = fibonacci(number)
    print(f"Факторіал числа {number} дорівнює {result}")
    print(f"{number}-те число Фібоначчі дорівнює {result1}")
    print(f"нсд чисел {number}, {number2} дорівнює {result2}")

if name == "__main__":
    main()
