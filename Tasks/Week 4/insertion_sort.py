"""
2. Insertion sort creates a sorted list by taking one element at a time and placing it 
in the correct position within the sorted section.
In the first snapshot, the list starts out mostly unsorted. As the sorting progresses, 
the sorted portion grows, which is reflected in the graph as the order improves.
In the animation, a red bar highlights the element being moved, showing exactly where 
it is being placed. This step-by-step process makes it clear how the sorting unfolds, 
as each iteration finds the right spot for the next element.
"""


def insertion_sort(array: list[int]) -> None:
    """Sorts `array` with insertion sort in-place."""
    n = len(array)
    for i in range(1, n):  # Outer loop starts from the second element
        insertee = array[i]  # Element to be placed in the correct position
        j = i

        # Move elements of the sorted portion that are greater than `insertee` to one position ahead
        while j > 0 and insertee < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1

        # Place the `insertee` at the correct position
        array[j] = insertee


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    insertion_sort(array)
    assert array == [1, 2, 3, 4, 5]
    print(array)
