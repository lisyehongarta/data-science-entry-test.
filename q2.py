Q2
Task 1:
def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val)
      in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

Answer:


if not isinstance(lst, list):
        return "Error: lst must be a list."

    # Create a new list with replaced values
    result = []
    for item in lst:
        if item == find_val:
            result.append(replace_val)
        else:
            result.append(item)

    return result



    Task 2:
# Invoke the function "find_and_replace" using the following scenarios: # - [1, 2, 3, 4, 2, 2], 2, 5 # - ["apple", "banana", "apple"], "apple", "orange" 

Answer: 
def find_and_replace(lst, old, new):
    for i in range(len(lst)):
        if lst[i] == old:
            lst[i] = new
    return lst

# Scenario 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)   # Output: [1, 5, 3, 4, 5, 5]

# Scenario 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)   # Output: ["orange", "banana", "orange"]

