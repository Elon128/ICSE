"""
1. Difference Between In-Place and Out-of-Place Sorting
In-place sorting refers to algorithms that sort data within the original array using only a small,
fixed amount of extra space. This typically means swapping elements within the same array. 
Out-of-place sorting, in contrast, requires additional memory, often to create a separate, 
sorted array, and thus duplicates the data temporarily.

3. Selection sort scans the list from left to right, looking for the smallest unsorted element.
Once found, it moves this smallest element to the sorted section on the left. The graphs in 
the first snapshot illustrate the sorting process step by step, with the list being sorted 
progressively from left to right. Each graph shows how much of the sorting is completed, 
making it easy to see the sorted portion grow. In the animated graph, red bars highlight the 
elements being compared or swapped. The animation shows each step in sequence, providing a 
clear view of how selection sort works from start to finish.
"""


def selection_sort(array: list[int]) -> None:
    """Sorts `array` with selection sort in-place."""
    n = len(array)
    for i in range(n - 1):  # Loop over each position in the array
        idx_min = i  # Assume the current position is the minimum
        for j in range(i + 1, n):  # Find the minimum element in the unsorted portion
            if array[j] < array[idx_min]:
                idx_min = j  # Update the index of the minimum element
        array[i], array[idx_min] = array[idx_min], array[i]  # Swap the found minimum


# Test the function
if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    selection_sort(array)
    print(array)
