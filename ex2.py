import sys
sys.setrecursionlimit(100000)
import random 
import time 
import matplotlib.pyplot as plt

sizes = [10, 20, 30]

# BUBBLE SORTimport sys sys.setrecursionlimit(20000)
#bubble sort seen in class
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr  


#chat gpt 
#def generate_case(size):
    #return {random.randint(0, 1000) for _ in range(size)}

# best: already sorted
#bestCaseBubble = sorted(generate_test_case(size))
# worst: reverse order
#worstCaseBubble = [size - i for i in range(size)]
# average: random order 
#averageCaseBubble = generate_case(size)

# QUICK SORT
 
#quick sort seen in class
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index+1, high)

#partitition function seen in class
def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left],
            arr[low], arr[right] = arr[right], arr[low]
    return right

# best: equal sized subarrays
#bestCaseQuick = [i for i in range(size)]
# worst: pivot is smallest or lagest element
#worstCaseQuick = sorted(generate_test_case(size))
# average: random initial order
#average_case_quick = generate_test_case(size)


def generate_bubble_case(size, case_type):
    if case_type == 'best':
        return sorted(list(range(size)))
    elif case_type == 'worst':
        return list(range(size, 0, -1))
    else:
        return [random.randint(0, 100) for _ in range(size)]

def test_bubble_algorithm(algorithm, array):
    start_time = time.time()
    algorithm(array)
    return time.time() - start_time

def generate_quick_case(size, case_type):
    if case_type == 'best':
        return [random.randint(0, 100)] * size  # Equal sized subarrays
    elif case_type == 'worst':
        pivot = random.choice([0, 100])
        return [pivot] * size  # Pivot is either smallest or largest element
    else:
        return [random.randint(0, 100) for _ in range(size)]  # Random initial order
    
def test_quick_algorithm(algorithm, array):
    start_time = time.time()
    algorithm(array, 0, len(array) - 1)
    return time.time() - start_time

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Test and plot for each case for both algorithms
for i, case_type in enumerate(['best', 'worst', 'average']):
    for size in sizes:
        # Bubble Sort
        bubble_array = generate_bubble_case(size, case_type)
        bubble_sort_time = test_bubble_algorithm(bubble_sort, bubble_array.copy())
        axes[0, i].plot(size, bubble_sort_time, 'ro-', label='Bubble Sort')

        # Quicksort
        quicksort_array = generate_quick_case(size, case_type)
        quicksort_time = test_quick_algorithm(quicksort, quicksort_array.copy())
        axes[1, i].plot(size, quicksort_time, 'bo-', label='Quicksort')

    axes[0, i].set_title(f'Bubble Sort - {case_type} case')
    axes[1, i].set_title(f'Quicksort - {case_type} case')

# Set common labels
for ax in axes.flat:
    ax.set(xlabel='Array Size', ylabel='Execution Time (seconds)')
    ax.legend()

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()


