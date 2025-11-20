Q4
def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return

Answer:
# Check if s is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    return s[::-1]   # This reverses the string

Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

Answer:

print(string_reverse("Hello World"))
print(string_reverse("Python"))
