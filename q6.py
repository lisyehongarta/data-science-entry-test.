Q6:
Task 1:

def find_first_negative(lst):
    """
    Task 1
    - Finds the first negative number in a list (lst).
    - Returns the first negative number if found, otherwise returns "No negatives".
    - Implemented using a while loop.
    """

Answer:

    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"

# Example usage:
print(find_first_negative([3, 5, -2, 7]))  # Output: -2
print(find_first_negative([1, 2, 3, 4]))   # Output: "No negatives"

Task 2:

# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

Answer: 

# Scenario 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(result1)  # Output: -1

# Scenario 2
result2 = find_first_negative([2, 10, 7, 0])
print(result2)  # Output: "No negatives"

