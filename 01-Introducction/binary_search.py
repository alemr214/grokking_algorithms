def binary_search(arr: list[int], number: int) -> int:
    """
    Búsqueda binaria en un arreglo de enteros.

    Args:
        arr (list[int]): Arreglo de enteros
        number (int): Número a buscar.

    Returns:
        int: Posición encontrada | (-1 si no se encuentra).
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        guess = arr[mid]

        if guess == number:
            return mid
        elif guess > number:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    number = 3

    result = binary_search(arr, number)
    print(result)  # 2


if __name__ == "__main__":
    main()
