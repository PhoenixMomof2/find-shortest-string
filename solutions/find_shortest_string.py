def find_shortest_string(arr):
    idx = 0
    min_length = len(arr[0])

    for i in range(len(arr)):
        if len(arr[i]) < min_length:
            min_length = len(arr[i])
            idx = i

    return arr[idx]

# Test the function
input_array = ["apple", "banana", "kiwi", "orange"]
shortest_string = find_shortest_string(input_array)
print(shortest_string) # Output: "kiwi"

def find_shortest_string(arr):
    shortest_string = min(arr, key=lambda x: len(x))
    return shortest_string

# Test the function
input_array = ["apple", "banana", "kiwi", "orange"]
shortest_string = find_shortest_string(input_array)
print(shortest_string) # Output: "kiwi"

'''In this optimized solution, the min function takes the list of strings (arr) and a lambda function lambda x: len(x) as arguments. The lambda function calculates the length of each string, and the min function uses this to find the shortest string in the list. The time complexity of finding the minimum element using min is O(n), but the overall time complexity of the function remains O(n) because it only needs to find the minimum once.

The space complexity of this optimized solution remains O(1) because it still uses only a constant amount of additional space to store the shortest string.'''