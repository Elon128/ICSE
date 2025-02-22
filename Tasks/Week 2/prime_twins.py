def is_prime(n: int) -> bool:
    """Checks if a number n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def prime_twins(n: int) -> list[tuple[int, int]]:
    """Returns the first n prime twins."""
    count = 0
    p = 3  # Start with the first prime number
    twins = []
    
    while count < n:
        q = p + 2
        if is_prime(p) and is_prime(q):
            twins.append((p, q))
            count += 1
        p += 2  # Move to the next odd number

    return twins


def prime_triplets(n: int) -> list[tuple[int, int, int]]:
    """Returns the first n prime triplets."""
    count = 0
    p = 3  # Start with the first prime number
    triplets = []
    
    while count < n:
        if is_prime(p) and is_prime(p + 2) and is_prime(p + 6):
            triplets.append((p, p + 2, p + 6))
            count += 1
        elif is_prime(p) and is_prime(p + 4) and is_prime(p + 6):
            triplets.append((p, p + 4, p + 6))
            count += 1
        p += 2  # Move to the next odd number

    return triplets


if __name__ == "__main__":
    # Test cases for prime twins
    assert prime_twins(2) == [(3, 5), (5, 7)]
    assert prime_twins(3) == [(3, 5), (5, 7), (11, 13)]
    
    # Test cases for prime triplets
    assert prime_triplets(1) == [(5, 7, 11)]
    assert prime_triplets(2) == [(5, 7, 11), (7, 11, 13)]
