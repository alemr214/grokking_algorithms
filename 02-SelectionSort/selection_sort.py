import random


def find_smallest(arr: list[int]) -> int:
    """
    Encuentra el elemento más chico en un arreglo

    Args:
        arr (list[int]): Arreglo de entrada

    Returns:
        int: index del elemento más chico
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list[int]) -> list[int]:
    """
    Algoritmo de ordenamiento de más chico a más grande

    Args:
        arr (list[int]): Arreglo inicial

    Returns:
        list[int]: Arreglo ordenado
    """
    new_arr = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
        smallest = find_smallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest))

    return new_arr


def main():
    n = 10
    my_array = [random.randint(1, 100) for _ in range(1, n)]
    print(f"Array original {my_array}")
    result = selection_sort(my_array)
    print(f"Array ordenado {result}")


if __name__ == "__main__":
    main()
