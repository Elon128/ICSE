def is_prime(n: int) -> bool:
    """Checks if a number n is a prime number."""
    if n <= 1:
        return False
    # Check divisors up to n-1
    for i in range(2, int(n - 1)):
        if n % i == 0:
            return False
    return True


def next_prime(n: int) -> int:
    """Finds the next prime number greater than or equal to n."""
    if n < 2:
        return 2

    # If `n` is prime, return `n`
    if is_prime(n):
        return n

    # Increment and check next prime numbers
    p: int = n + 1
    while not is_prime(p):
        p += 1

    return p

""" Best & Worst Case Runtime Complexity for Given Code

1. is_prime(n: int) -> bool
	•	Best Case: O(1) (If n <= 1, the function returns immediately)
	•	Worst Case: O(n) (Iterates up to n-1 checking divisibility)

2. next_prime(n: int) -> int
	•	Best Case: O(1) (If n is already prime, it returns immediately)
	•	Worst Case: O(n²) (In the worst case, checking multiple non-prime numbers using is_prime(n), each taking up to O(n))
 """