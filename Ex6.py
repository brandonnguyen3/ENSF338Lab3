# 1. Implementation of binary and linear search 
# Linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Element not found
# Quick Sort with Binary
# Define the quicksort and binary search functions
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

def quicksort_and_binary_search(arr, target):
    sorted_arr = quicksort(arr)
    index = binary_search(sorted_arr, target)
    return index
# 2. Then, measure their performance on 100 random tasks. An appropriate random task here would be to search for a constant
# element in an array that gets reshuffled every time.
import random
import time

# Define linear search function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Element not found

# Define quicksort and binary search functions
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# Perform 100 random tasks
total_linear_time = 0
total_quicksort_time = 0

for _ in range(100):
    # Generate a random array
    arr = [random.randint(1, 1000) for _ in range(1000)]

    # Shuffle the array
    random.shuffle(arr)

    # Choose a random target element
    target = random.choice(arr)

    # Measure linear search time
    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    total_linear_time += end_time - start_time

    # Measure quicksort and binary search time
    start_time = time.time()
    sorted_arr = quicksort(arr)
    binary_search(sorted_arr, target)
    end_time = time.time()
    total_quicksort_time += end_time - start_time

# Calculate average time for each algorithm
average_linear_time = total_linear_time / 100
average_quicksort_time = total_quicksort_time / 100

print(f"Average time for linear search: {average_linear_time} seconds")
print(f"Average time for quicksort and binary search: {average_quicksort_time} seconds")
# 3. You must redo the above with inputs of size 10, 20, 50, 100, 200,500, 1000, 2000, 5000, 10000 
import random
import time

# Define linear search function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Element not found

# Define quicksort and binary search functions
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# Perform tasks for different input sizes
input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for size in input_sizes:
    # Perform 100 random tasks for each input size
    total_linear_time = 0
    total_quicksort_time = 0

    for _ in range(100):
        # Generate a random array of the current size
        arr = [random.randint(1, 1000) for _ in range(size)]

        # Shuffle the array
        random.shuffle(arr)

        # Choose a random target element
        target = random.choice(arr)

        # Measure linear search time
        start_time = time.time()
        linear_search(arr, target)
        end_time = time.time()
        total_linear_time += end_time - start_time

        # Measure quicksort and binary search time
        start_time = time.time()
        sorted_arr = quicksort(arr)
        binary_search(sorted_arr, target)
        end_time = time.time()
        total_quicksort_time += end_time - start_time

    # Calculate average time for each algorithm
    average_linear_time = total_linear_time / 100
    average_quicksort_time = total_quicksort_time / 100

    print(f"Input Size: {size}")
    print(f"Average time for linear search: {average_linear_time} seconds")
    print(f"Average time for quicksort and binary search: {average_quicksort_time} seconds")
    print()
    #4 Plot the above
import random
import time
import matplotlib.pyplot as plt

# Define linear search function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Element not found

# Define quicksort and binary search functions
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# Perform tasks for different input sizes
input_sizes = [10, 100, 500, 1000, 2000, 5000, 10000]

linear_search_times = []
binary_search_times = []

# Shuffle the array once for all input sizes
arr = [random.randint(1, 1000) for _ in range(max(input_sizes))]
random.shuffle(arr)

for size in input_sizes:
    # Perform 100 random tasks for each input size
    total_linear_time = 0
    total_binary_time = 0

    for _ in range(100):
        # Choose a random target element
        target = random.choice(arr[:size])  # Use only part of the shuffled array

        # Measure linear search time
        start_time = time.time()
        linear_search(arr[:size], target)  # Use only part of the shuffled array
        end_time = time.time()
        total_linear_time += end_time - start_time

        # Measure binary search time
        start_time = time.time()
        binary_search(quicksort(arr[:size]), target)  # Use only part of the shuffled array
        end_time = time.time()
        total_binary_time += end_time - start_time

    # Calculate average time for each algorithm
    average_linear_time = total_linear_time / 100
    average_binary_time = total_binary_time / 100

    linear_search_times.append(average_linear_time)
    binary_search_times.append(average_binary_time)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, linear_search_times, marker='o', label='Linear Search')
plt.plot(input_sizes, binary_search_times, marker='o', label='Binary Search (Quicksort)')
plt.title('Performance Comparison: Linear Search vs. Binary Search (Quicksort)')
plt.xlabel('Input Size')
plt.ylabel('Average Time (seconds)')
plt.xscale('log')
plt.xticks(input_sizes, rotation=45)
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()
plt.show()
