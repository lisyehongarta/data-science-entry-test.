Q3:
Task 1

def update_dictionary(dct, key, value):
    """
    - Update dictionary with a new key-value pair.
    - If key already exists, print the original value first.
    - Return the updated dictionary.
    """

Answer:

    if key in dct:
        print("Original value:", dct[key])
    
    dct[key] = value
    return dct

Task 2
# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

Answer:

def update_dictionary(dct, key, value):
    if key in dct:
        print("Original value:", dct[key])
    dct[key] = value
    return dct

# Task 2
# Invoke the function using the given scenarios

# Scenario 1
result1 = update_dictionary({}, "name", "Alice")
print(result1)

# Scenario 2
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)
