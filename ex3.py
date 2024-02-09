
#Used ChatGPT
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            # If no swaps were made in the current pass, the array is already sorted
            break
    return comparisons, swaps

def generate_partially_sorted_array(n):
    arr = list(range(n))
    # Introduce some randomness by swapping elements
    for i in range(n // 10):
        idx1 = random.randint(0, n-1)
        idx2 = random.randint(0, n-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

def generate_nearly_sorted_array(n):
    arr = list(range(n))
    # Introduce some randomness by swapping adjacent elements
    for i in range(n // 10):
        idx = random.randint(0, n-2)
        arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
    return arr

def run_bubble_sort_analysis():
    sizes = [10, 50, 100, 500, 1000, 5000]  # Sizes of input arrays
    comparison_results = []
    swap_results = []
    for size in sizes:
        input_array = generate_partially_sorted_array(size)
        comparisons, swaps = bubble_sort(input_array.copy())
        comparison_results.append(comparisons)
        swap_results.append(swaps)

    return sizes, comparison_results, swap_results

def plot_results(sizes, comparison_results, swap_results):
    # Plotting comparisons
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(sizes, comparison_results, 'bo', label='Actual')
    plt.xlabel('Input Size')
    plt.ylabel('Number of Comparisons')
    plt.title('Number of Comparisons vs Input Size')

    # Fitting a quadratic curve to comparisons
    def quadratic_curve(x, a, b, c):
        return a * x**2 + b * x + c

    popt, _ = curve_fit(quadratic_curve, sizes, comparison_results)
    sizes_fit = np.linspace(min(sizes), max(sizes), 100)
    comparisons_fit = quadratic_curve(sizes_fit, *popt)
    plt.plot(sizes_fit, comparisons_fit, 'r-', label='Quadratic Fit')

    plt.legend()

    # Plotting swaps
    plt.subplot(1, 2, 2)
    plt.plot(sizes, swap_results, 'bo', label='Actual')
    plt.xlabel('Input Size')
    plt.ylabel('Number of Swaps')
    plt.title('Number of Swaps vs Input Size')

    # Fitting a quadratic curve to swaps
    def quadratic_curve(x, a, b, c):
        return a * x**2 + b * x + c

    popt, _ = curve_fit(quadratic_curve, sizes, swap_results)
    swaps_fit = quadratic_curve(sizes_fit, *popt)
    plt.plot(sizes_fit, swaps_fit, 'r-', label='Quadratic Fit')

    plt.legend()

    plt.tight_layout()
    plt.show()

sizes, comparison_results, swap_results = run_bubble_sort_analysis()
plot_results(sizes, comparison_results, swap_results)
