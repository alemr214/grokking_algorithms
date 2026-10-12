def sum(arr: list[int]) -> int:
    """
    Suma de los valores de un arreglo

    Args:
        arr (list[int]): Arreglo de entrada

    Returns:
        int: Valor de la suma
    """
    copied_arr = list(arr)
    if len(copied_arr) == 0:
        return 0
    elif len(copied_arr) == 1:
        return copied_arr[0]
    else:
        return copied_arr.pop(0) + sum(copied_arr)


def main():
    n = 5
    my_array = [x for x in range(1, n)]
    result = sum(my_array)
    print(f"La suma del arreglo {my_array} es {result}")


if __name__ == "__main__":
    main()
