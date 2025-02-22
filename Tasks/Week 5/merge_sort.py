"""
1.  Divide and Conquer:
Divide and conquer is a strategy where a problem is broken into smaller sub-problems, solved 
independently, and their solutions are combined to solve the original problem. Merge sort uses 
this approach by dividing the array into smaller sub-arrays, sorting them recursively, and merging 
the results.

2.  Stable Sorting:
A sorting algorithm is stable if it preserves the relative order of elements with equal values in 
the original array. Merge sort is a stable algorithm because it does not reorder equal elements 
while merging.

Example of Merge Sort on [5, 3, 2, 7, 6, 9, 1, 8, 4, 10]:

Step 1: Dividing the Array
[5, 3, 2, 7, 6, 9, 1, 8, 4, 10]
[5, 3, 2, 7, 6] [9, 1, 8, 4, 10]
[5, 3] [2, 7, 6] [9, 1] [8, 4, 10]
[5] [3] [2] [7] [6] [9] [1] [8] [4] [10]

Step 2: Merging Subarrays
[3, 5] [2, 6, 7] [1, 9] [4, 8, 10]
[2, 3, 5, 6, 7] [1, 4, 8, 9, 10]

Step 3: Final Merge
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Combine two sorted lists into a single sorted list.
    """
    result = []  # A new list to store the merged result
    i, j = 0, 0  # Start pointers for both lists

    # Compare elements from both lists and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # Take from 'left' if it's smaller
            result.append(left[i])
            i += 1
        else:  # Otherwise, take from 'right'
            result.append(right[j])
            j += 1

    # Add the remaining elements from either list
    result.extend(left[i:])  # If anything is left in 'left'
    result.extend(right[j:])  # If anything is left in 'right'
    return result


def merge_sort(array: List[int]) -> List[int]:
    """
    Sort a list using merge sort and return a new sorted list.
    """
    if len(array) <= 1:  # Base case: A single item is already sorted
        return array

    # Divide the list into two halves
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])  # Sort the first half
    right_half = merge_sort(array[mid:])  # Sort the second half

    # Combine the sorted halves
    return merge(left_half, right_half)


if __name__ == "__main__":
    # Input array
    array = [5, 3, 2, 7, 6, 9, 1, 8, 4, 10]

    # Call the merge sort function
    sorted_array = merge_sort(array)

    # Print the results
    print("Original array:", array)  # The original array stays the same
    print("Sorted array:", sorted_array)  # The sorted version of the array
