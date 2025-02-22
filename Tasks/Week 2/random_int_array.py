import random


def create_random(n: int) -> list[int]:
    """Creates an array with `n` random integers in the range `[5, 99]`."""
    random_array = []
    for _ in range(n):
        random_num = random.randint(5, 99)
        random_array.append(random_num)
    return random_array


def to_string(a: list[int]) -> str:
    """Creates a string from an array."""
    result = ""
    for i in range(len(a)):
        result += str(a[i])
        if i < len(a) - 1:  # List indexing is zero-based
            result += ", "
    return result


def pos_min(a: list[int]) -> int:
    """
    Returns the position of the smallest element in `a`. If it is not unique, it
    returns the position of the first one.
    """
    if len(a) == 0:
        return -1  # Return -1 in case of empty array
    
    min_index = 0  # Assume first element is min
    for i in range(1, len(a)):
        if a[i] < a[min_index]:
            min_index = i
    return min_index


def swap(a: list[int]) -> None:
    """Swaps the first and last element in `a`."""
    if len(a) > 1:
        a[0], a[-1] = a[-1], a[0]


if __name__ == "__main__":
    size = 5
    random_array = create_random(size)
    print("Random Array:", to_string(random_array))
    print("Position of Minimum:", pos_min(random_array))
    swap(random_array)
    print("Array after Swap:", to_string(random_array))
