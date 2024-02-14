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
import time
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(sorted_arr, target):
    low, high = 0, len(sorted_arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for size in input_sizes:
    total_linear_time = 0
    total_quicksort_time = 0

    for _ in range(100):
        arr = [random.randint(1, 1000) for _ in range(size)]

        # Separate shuffle for each iteration
        random.shuffle(arr)

        target = random.choice(arr)

        # Measure linear search time
        start_time = time.time()
        linear_search(arr, target)
        end_time = time.time()
        total_linear_time += end_time - start_time

        # Separate shuffle for quicksort
        arr = [random.randint(1, 1000) for _ in range(size)]
        random.shuffle(arr)

        # Measure quicksort and binary search time
        start_time = time.time()
        sorted_arr = quicksort(arr)
        binary_search(sorted_arr, target)
        end_time = time.time()
        total_quicksort_time += end_time - start_time

    average_linear_time = total_linear_time / 100
    average_quicksort_time = total_quicksort_time / 100

    print(f"Input Size: {size}")
    print(f"Average time for linear search: {average_linear_time} seconds")
    print(f"Average time for quicksort and binary search: {average_quicksort_time} seconds")
    print()
# 4. plot the above
import timeit
import random
import matplotlib.pyplot as plt

def linear_search(target, arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(target, sorted_arr):
    low, high = 0, len(sorted_arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

avgtimes_linear = []
avgtimes_binary = []

# For the specified input sizes
input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for listlength in input_sizes:
    # Generate a list of that input length
    numbers = [x for x in range(listlength)]
    
    # Measure average time for linear search
    linear_avg_time = timeit.timeit(lambda: random.shuffle(numbers) and linear_search(5, numbers), number=100) / 100
    avgtimes_linear.append(linear_avg_time)
    
    # Measure average time for binary search with quicksort
    sorted_numbers = quicksort(numbers)
    binary_avg_time = timeit.timeit(lambda: random.shuffle(numbers) and binary_search(5, sorted_numbers), number=100) / 100
    avgtimes_binary.append(binary_avg_time)

    print("Average time for list of length %d:" % listlength)
    print("Linear Search: %f" % linear_avg_time)
    print("Binary Search: %f\n" % binary_avg_time)

# Plotting
plt.plot(input_sizes, avgtimes_linear, label='Linear Search')
plt.plot(input_sizes, avgtimes_binary, label='Binary Search with Quicksort')
plt.xlabel('Input Size')
plt.ylabel('Average Time (seconds)')
plt.title('Comparison of Linear and Binary Search')
plt.legend()
plt.show()

#Based on the plot generated by the code above and in general we can see that the binary serach works faster for larger sizes of data whereas
# linear search works faster with smaller data sizes. As the size of data increases the execution time for linear serach increases and the execution time
# binary serach decreases.
