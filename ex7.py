#ENSF 338 Lab 3: Exercise 7
import json
import timeit
import matplotlib.pyplot as plt

import sys 
sys.setrecursionlimit(20000)

'''
1. Implement a standard binary search, with the following tweak: the
midpoint for the first iteration must be configurable (all successive
iterations will just split the array in the middle) [0.2 pts]
'''
def binary_search(arr, target, low, high, n):
    # Base case: if low is greater than high, the element is not present
    if low > high:
        return -1
    
    mid = (low + high) // n
    
    # If target is present at mid
    if arr[mid] == target:
        return mid
    # If target is greater, search in the right half
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high, 2)
    # If target is smaller, search in the left half
    else:
        return binary_search(arr, target, low, mid - 1, 2)


# Read array from ex7data.json
with open('ex7data.json') as f:
    arr = json.load(f)
# Read search tasks from ex7tasks.json
with open('ex7tasks.json') as f:
    tasks = json.load(f)


# Function to handle search tasks
    
def search1(arr, tasks):
    results = []
    for target in tasks:
        start_time = timeit.default_timer()  # Start timing
        result = binary_search(arr, target, 0, len(arr) - 1, 1)
        end_time = timeit.default_timer()    # Stop timing
        execution_time = end_time - start_time
        if result != -1:
            results.append((target, execution_time))
    return results

def search2(arr, tasks):
    results = []
    for target in tasks:
        start_time = timeit.default_timer()  # Start timing
        result = binary_search(arr, target, 0, len(arr) - 1, 2)
        end_time = timeit.default_timer()    # Stop timing
        execution_time = end_time - start_time
        if result != -1:
            results.append((target, execution_time))
    return results

def search3(arr, tasks):
    results = []
    for target in tasks:
        start_time = timeit.default_timer()  # Start timing
        result = binary_search(arr, target, 0, len(arr) - 1, 3)
        end_time = timeit.default_timer()    # Stop timing
        execution_time = end_time - start_time
        if result != -1:
            results.append((target, execution_time))
    return results

# Perform search tasks for n = 1, n = 2, n = 3
results1 = search1(arr, tasks)
results2 = search2(arr, tasks)
results3 = search3(arr, tasks)

# Extract input values and corresponding execution times
task_values = [result[0] for result in results2]

execution_times1= [result[1] for result in results2]
execution_times2 = [result[1] for result in results2]
execution_times3 = [result[1] for result in results3]

'''
2. Time the performance of each search task w/ different midpoints
for each task. You can use whatever strategy you want to check
different midpoints. Then, choose the best midpoint for each task
'''

best_midpoints = {}
for target in tasks:
    min_time = float('inf')
    best_midpoint = None
    for n, results_n in [(1, results1), (2, results2), (3, results3)]:
        for task, time in results_n:
            if task == target and time < min_time:
                min_time = time
                best_midpoint = n
    best_midpoints[target] = best_midpoint


# prints out the best midpoint
print("Best Midpoints:")
for target, best_midpoint in best_midpoints.items():
    print(f"Target: {target}, Best Midpoint: {best_midpoint}")


'''
Graphs the results
'''
plt.scatter(task_values, execution_times1, label='Midpoint is 1/1')
plt.scatter(task_values, execution_times2, label='Midpoint is 1/2')
plt.scatter(task_values, execution_times3, label='Midpoint is 1/3')

plt.xlabel('Task Values')
plt.ylabel('Execution Times')
plt.title('Scatter Plot of Execution Times against Task Values')
plt.legend()
plt.grid(True)
plt.show()

'''
4. Comment on the graph. Does the choice of initial midpoint appear
to affect performance? Why do you think is that?

Overall the choice of initial midpoint does not appear to affect the performance in any noticable way. 
All of the values seem to be clumped together in one straight line, and there doesn't seem 
to be any noticable difference between all three graphs, with the exception of a few outliers.
This is to be expected. If the search value is approximately random, we should expect that regardless of midpoint
that they should all be quite similar. 
'''

