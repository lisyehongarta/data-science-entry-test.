Q1
def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
Answer: 

    # Swap values using arithmetic operations (without a temporary variable)
    x = x + y
    y = x - y  # y now holds the original value of x
    x = x - y  # x now holds the original value of y

    print(f"Swapped values: x = {x}, y = {y}")

# Test cases
print("--- Test Case 1: Numeric values ---")
swap(5, 10)

print("\n--- Test Case 2: Numeric values (floats) ---")
swap(3.14, 2.71)

print("\n--- Test Case 3: Non-numeric x ---")
result = swap("hello", 100)
print(f"Return value for non-numeric x: {result}")

print("\n--- Test Case 4: Non-numeric y ---")
result = swap(20, "world")
print(f"Return value for non-numeric y: {result}")

print("\n--- Test Case 5: Both non-numeric ---")
result = swap("a", "b")
print(f"Return value for both non-numeric: {result}")


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

Answer:

def swap(a, b):
    print(f"Original values: a={a}, b={b}")
    print(f"Swapped values: a={b}, b={a}")

print("Scenario 1: 'Apple', 10")
swap("Apple", 10)

print("\nScenario 2: 9, 17")
swap(9, 17)


