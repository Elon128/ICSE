# Task 1
def median(a: int, b: int, c: int) -> int:
    """Returns the median of three integers a, b, and c."""
    if (b <= a <= c) or (c <= a <= b):
        return a
    elif (a <= b <= c) or (c <= b <= a):
        return b
    else:
        return c


# Task 2
# Return the second element after sorting
def median2(a: int, b: int, c: int) -> int:
    """Returns the median of three integers a, b, and c by sorting."""
    return sorted([a, b, c])[1]


def run_tests():
    """Runs a set of test cases to validate the median functions."""
    test_cases = [
        (25, 11, 33, 25),
        (1, 1, 2, 1),
        (3, 7, 5, 5),
        (9, 5, 9, 9),
        (10, 10, 10, 10),
    ]
    # Takes only 3 values in each tuple
    for a, b, c, expected in test_cases:
        print(f"median({a}, {b}, {c}) = {median(a, b, c)}")
        print(f"median2({a}, {b}, {c}) = {median2(a, b, c)}\n")


# To ensure the test function does not run when code is imported to another file
if __name__ == "__main__":
    run_tests()
