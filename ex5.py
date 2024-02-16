'''
Question 4
As the size increases past 100, binary insertion tends to 
out perform insertion sort. Insertion sort tends only to be
faster for small input sizes. 
'''
import time
import random
import matplotlib.pyplot as plt

sizes = [50, 100, 240, 500]

#seen in class
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
#use chatgpt
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        low, high = 0, i - 1

        while low <= high:
            mid = (low + high) // 2
            if key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        arr[low + 1:i + 1] = arr[low:i]
        arr[low] = key

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time

def generate_avg_case(size):
    return [random.randint(0, 100) for _ in range(size)]
#enf of chatgpt
        
insertion_sort_times = []
binary_insertion_sort_times = []

for size in sizes:
    data = generate_avg_case(size)

    insertion_time = measure_time(insertion_sort, data.copy())
    insertion_sort_times.append(insertion_time)

    binary_insertion_time = measure_time(binary_insertion_sort, data.copy())
    binary_insertion_sort_times.append(binary_insertion_time)

# Plot the results
plt.plot(sizes, insertion_sort_times, label="Insertion Sort")
plt.plot(sizes, binary_insertion_sort_times, label="Binary Insertion Sort")
plt.xlabel("Size of input")
plt.ylabel("Time taken")
plt.legend()
plt.show()
