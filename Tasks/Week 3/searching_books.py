# Question 1: Linear Search
def search_linear(a: list[str], item: str) -> int | None:
    """Linear search to find the position of the item in the list."""
    
    for i in range(len(a)):
        if a[i] == item:
            return i  # Return the index if item is found
    return None  # If loop completes and item isn't found, return None


# Question 2: Binary Search
def search_binary(a: list[str], item: str) -> int | None:
    """Binary search to find the position of the item in a sorted list."""
    
    left, right = 0, len(a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == item:
            return mid
        elif a[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return None  # Return None if the item is not found


# Question 3: Linear Search with Comparison Count
def search_linear_cmp_count(a: list[str], item: str) -> int:
    """Count comparisons in a linear search for the item in the list."""
    
    comparisons = 0
    
    for i in range(len(a)):
        comparisons += 1
        if a[i] == item:
            return comparisons  # Return the count of comparisons if item is found
    
    return comparisons  # Return total comparisons if item is not found


# Question 4: Binary Search with Comparison Count
def search_binary_cmp_count(a: list[str], item: str) -> int:
    """Count comparisons in a binary search for the item in a sorted list."""
    
    comparisons = 0
    left, right = 0, len(a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        
        if a[mid] == item:
            return comparisons  # Return comparisons if item is found
        elif a[mid] < item:
            comparisons += 1
            left = mid + 1
        else:
            comparisons += 1
            right = mid - 1

    return comparisons  # Return total comparisons if item is not found


# Test cases
books1 = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
books2 = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb"]
book_to_find = "cc"

# Testing Linear and Binary Search with Comparison Count
print("Linear Search Comparisons:")
print(search_linear_cmp_count(books1, book_to_find))
print(search_linear_cmp_count(books2, book_to_find))

print("Binary Search Comparisons:")
print(search_binary_cmp_count(books1, book_to_find))
print(search_binary_cmp_count(books2, book_to_find))
