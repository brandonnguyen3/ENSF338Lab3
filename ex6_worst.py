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
    # Generate a sorted list of that input length to induce worst-case for quicksort
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
plt.plot(input_sizes, avgtimes_binary, label='Binary Search with Quicksort (Worst-case)')
plt.xlabel('Input Size')
plt.ylabel('Average Time (seconds)')
plt.title('Comparison of Linear and Binary Search (Worst-case for Quicksort)')
plt.legend()
plt.show()
