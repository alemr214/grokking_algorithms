def factorial(number: int) -> int:
    """
    Funcion para calcular factorial con recursion

    Args:
        number (int): Numero base

    Returns:
        int: Factorial del numero base
    """
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def main() -> None:
    number = 5
    result = factorial(number)
    print(f"Factorial de {number} es {result}")


if __name__ == "__main__":
    main()
