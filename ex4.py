#ENSF 338 Lab 3 ex4.py
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import sys 
sys.setrecursionlimit(20000)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def generate_worst_case_input(n):
    # Generate an array with elements in decreasing order
    return list(range(n, 0, -1))

def run_quicksort_analysis():
    sizes = [10, 50, 100, 500, 1000, 5000]  # Sizes of input arrays
    time_results = []
    for size in sizes:
        input_array = generate_worst_case_input(size)
        start_time = time.time()
        quicksort(input_array, 0, size - 1)
        end_time = time.time()
        time_results.append(end_time - start_time)

    return sizes, time_results

def plot_results(sizes, time_results):
    # Plotting time taken
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, time_results, 'bo', label='Actual')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Worst-Case Complexity')
    
    # Fitting a quadratic curve to time results
    def quadratic_curve(x, a, b, c):
        return a * x**2 + b * x + c

    popt, _ = curve_fit(quadratic_curve, sizes, time_results)
    sizes_fit = np.linspace(min(sizes), max(sizes), 100)
    time_fit = quadratic_curve(sizes_fit, *popt)
    plt.plot(sizes_fit, time_fit, 'r-', label='Quadratic Fit')

    plt.legend()
    plt.show()

sizes, time_results = run_quicksort_analysis()
plot_results(sizes, time_results)
