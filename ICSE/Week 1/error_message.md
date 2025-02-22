# Error message fixes

# Script 1
# SyntaxError: '(' was never closed
print("This is a simple test")  # Added missing ")"
print("Oha, it does not work.")

# Script 2
# NameError: name 'gravitational_acceleration' is not defined
mass_in_kg = 10
gravitational_acceleration = 9.81  # Defined gravitational_acceleration
force = mass_in_kg * gravitational_acceleration

print(f"{mass_in_kg} kg gets accelerated with a force of {force} N on earth.")

# Script 3
# ModuleNotFoundError: No module named 'Math'
from math import sqrt  # Corrected to lowercase 'math'
a = 9
print(f"The square root of {a} is {sqrt(a)}.")

# Script 4
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("Let's run some legacy code...")  # Added parentheses

# Script 5
# TypeError: can't multiply sequence by non-int of type 'float'
print("Let's repeat this" * 3)  # Changed to integer 3

# Script 6
# IndentationError: unindent does not match any outer indentation level
age = int(input("Your age: "))

if age < 18:
    print("Sorry, we don't serve minors here")
else:  # Aligned else with if
    print("What can I serve you?")

# Script 7
# SyntaxError: expected ':'
while input("What can I serve you? ") != "Gin":  # Added ":"
    print("Awful choice, try again.")
print("Good choice.")

# Bonus
# Adding if __name__ == "__main__": ensures that run_tests() only runs when executed directly
