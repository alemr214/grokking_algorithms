import random


def find_highest(arr: list[int]) -> int | None:
    """
    Encuentra el valor más alto de un arreglo

    Args:
        arr (list[int]): Arreglo de entrada

    Returns:
        int | None: Valor más alto
    """
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        if arr[0] > arr[1]:
            arr.pop(1)
            return find_highest(arr[:])
        else:
            return find_highest(arr[1:])


def main():
    my_arr = [random.randint(1, 20) for _ in range(10)]
    result = find_highest(my_arr)
    print(f"El valor más alto en el arreglo {my_arr} es {result}")


if __name__ == "__main__":
    main()
