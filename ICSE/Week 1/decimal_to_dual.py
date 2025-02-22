def transform_to_dual(dec: int) -> str:
    """Transforms a decimal number to its binary representation as a string."""
    output = ""  # This will store the binary result

    if dec == 0:  # Special case: if the number is 0, just return "0"
        return "0"

    while dec > 0:
        remainder = dec % 2  # Get the remainder (0 or 1)
        output = str(remainder) + output  # Add the remainder to the left of output
        dec = dec // 2  # Halve the number for the next iteration

    return output


if __name__ == "__main__":
    # Testing with some examples
    print(transform_to_dual(13))
    print(transform_to_dual(0))
    print(transform_to_dual(1))
    print(transform_to_dual(10))
