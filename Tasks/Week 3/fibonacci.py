# Solution for part 2

# Recursive function to calculate the n-th Fibonacci number
number_recursive_calls = 0


def fib1(n: int) -> int:
    global number_recursive_calls
    number_recursive_calls += 1  # Increment the counter on each call
    if n == 0 or n == 1:
        return 1
    else:
        return fib1(n - 2) + fib1(n - 1)


# Test case
print(fib1(1))
print(fib1(4))


# Generate and print the first 15 Fibonacci numbers
fibonacci_list = []
for i in range(15):
    fibonacci_list.append(fib1(i))  # Append each Fibonacci number to the list

print(fibonacci_list)  # Output the list of the first 15 Fibonacci numbers


# Fibonacci Series using iteration (fib2)

number_loop_iterations = 0


def fib2(n: int) -> int:
    global number_loop_iterations
    if n == 0 or n == 1:
        number_loop_iterations += 1
        return 1
    else:
        a, b = 1, 1  # Starting values for fib(0) and fib(1)
        for _ in range(2, n + 1):
            a, b = b, a + b  # Update values for next Fibonacci number
            number_loop_iterations += 1  # Increment the counter on each iteration
        return b


# Test case
print(fib2(5))


# Calculate and display results for the 23rd Fibonacci number
if __name__ == "__main__":
    # Reset counter for recursive calls
    number_recursive_calls = 0
    
    # Calculate the 23rd Fibonacci number using fib1_with_count
    fib1_result = fib1(23)
    print(fib1_result)
    print(number_recursive_calls)

    # Calculate the 23rd Fibonacci number using fib2_with_count
    number_loop_iterations = 0
    fib2_result = fib2(23)
    print(fib2_result)
    print(number_loop_iterations)
