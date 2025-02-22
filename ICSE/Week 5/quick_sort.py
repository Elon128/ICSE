"""
2. First Plot (Subplots):
The subplots illustrate the step-by-step process of how quicksort partitions the array.
Initially, at 0% progress, the array remains completely unsorted. As sorting advances
(e.g., 20%), a pivot is chosen, and elements are repositioned on either side of it based
on comparison. By the time sorting reaches 100% progress, all subarrays are fully processed,
and the array becomes completely sorted.

Second Plot (Single Histogram):
This plot highlights the changes in the array during partitioning at a specific iteration.
The red bars represent pivot elements or elements involved in comparisons, emphasizing the
elements being swapped as the array gets partitioned.

3. Best Case:
When the pivot divides the array into perfectly balanced partitions, the algorithm performs
efficiently with a time complexity of O(n log n).

Worst Case:
If the pivot happens to be the smallest or largest element, it creates highly unbalanced
partitions, leading to a time complexity of O(n^2).
"""


def quick_sort(array: list[int]) -> None:
    """Sorts the given array in-place using the Quick Sort algorithm."""
    def quick_sort_recursive(low: int, high: int) -> None:
        if low < high:
            # Partition the array
            pivot_index = partition(low, high)
            # Recursively sort the two halves
            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)

    def partition(low: int, high: int) -> int:
        """Partitions the array using the last element as the pivot."""
        pivot = array[high]  # Choose the last element as pivot
        i = low - 1          # Pointer for the smaller element

        for j in range(low, high):
            if array[j] <= pivot:  # If current element is less than or equal to pivot
                i += 1
                array[i], array[j] = array[j], array[i]  # Swap

        # Place the pivot in the correct position
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1  # Return pivot index

    # Start the recursive Quick Sort with the entire array
    quick_sort_recursive(0, len(array) - 1)


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    quick_sort(array)
    print(array)  # Output the sorted array
