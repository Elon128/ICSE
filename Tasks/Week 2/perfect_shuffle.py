def interleave(a: list[int], b: list[int]) -> list[int]:
    """
    Returns a new array with elements consecutively taken from array `a` and `b`.
    """
    mix = []  # Initialize an empty list
    for i in range(len(a)):
        mix.append(a[i])
        mix.append(b[i])
    return mix


def perfect_shuffle(a: list[int]) -> list[int]:
    """Returns a new array that is perfectly shuffled once."""
    if len(a) % 2 != 0:
        raise ValueError("The array must have an even number of elements.")
    mid = len(a) // 2  # Split the array into two halves using slicing
    a1 = a[:mid]
    b1 = a[mid:]
    return interleave(a1, b1)


def shuffle_number(n: int) -> int:
    """Returns the number of perfect shuffles needed to return the deck to its original order."""
    original_deck = list(range(n))  # To compare original deck and shuffled deck
    shuffled_deck = original_deck[:]
    count = 0

    while True:
        shuffled_deck = perfect_shuffle(shuffled_deck)  # Keep shuffling until the deck returns to its original order
        count += 1
        if shuffled_deck == original_deck:
            break

    return count


# Example usage
if __name__ == "__main__":
    print(shuffle_number(52))

""" Best & Worst Case Runtime Complexity for Given Code

1. interleave(a: list[int], b: list[int])
	•	Best Case: O(n) (Iterates over n/2 elements twice, effectively O(n))
	•	Worst Case: O(n) (Always processes all elements of both lists)

2. perfect_shuffle(a: list[int])
	•	Best Case: O(n) (Splitting and interleaving both take O(n))
	•	Worst Case: O(n) (No variations; always runs in O(n))

3. shuffle_number(n: int)
	•	Best Case: O(n) (If the array returns to original order after one shuffle)
	•	Worst Case: O(n log n) (It can take log n iterations to cycle back, with each shuffle being O(n)) """