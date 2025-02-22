"""
3. Bubble sort works by repeatedly comparing two adjacent elements and swapping them if they are in the wrong order.
With each pass, the largest unsorted element moves to its correct position at the end of the list, like its
“bubbling up.” This process continues until no swaps are needed, indicating the list is completely sorted.

In the first plot, the elements start in random order. As sorting progresses (e.g., 20%, 40%, 60%, 80%), the sorted
section grows from right to left. By the final plot, all elements are arranged in ascending order. The animation
visually highlights each comparison and swap, step by step, making it easy to see how Bubble Sort gradually organizes
the list.
"""


def bubble_sort(array: list[int]) -> None:
    """Sorts `array` with bubble sort in-place."""
    n = len(array)
    for i in range(n - 1, 0, -1):  # Outer loop iterates over the array in reverse
        for j in range(1, i + 1):  # Inner loop compares adjacent elements
            if array[j - 1] > array[j]:  # Swap if they are in the wrong order
                array[j - 1], array[j] = array[j], array[j - 1]


if __name__ == "__main__":
    # Test the bubble_sort function
    array = [3, 2, 4, 1, 5]
    bubble_sort(array)
    assert array == [1, 2, 3, 4, 5]  # Verify the array is sorted correctly
    print(array)  # Output the sorted array
