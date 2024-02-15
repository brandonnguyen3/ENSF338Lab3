import random
import matplotlib.pyplot as plt
import timeit

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_worst_case(size):
    return list(range(size, 0, -1))

def generate_best_case(size):
    return list(range(1, size+1))

def generate_random_case(size):
    return [random.randint(0, 1000) for _ in range(size)]

def test_sorting_algorithms():
    sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800]
    bubble_sort_times_worst = []
    quick_sort_times_worst = []
    bubble_sort_times_best = []
    quick_sort_times_best = []

    for size in sizes:
        # Worst case
        worst_case_arr = generate_worst_case(size)
        bubble_arr = worst_case_arr.copy()
        bubble_time_worst = timeit.timeit(lambda: bubble_sort(bubble_arr), number=1)
        bubble_sort_times_worst.append(bubble_time_worst)

        quick_arr = worst_case_arr.copy()
        quick_time_worst = timeit.timeit(lambda: quick_sort(quick_arr), number=1)
        quick_sort_times_worst.append(quick_time_worst)

        # Best case
        best_case_arr = generate_best_case(size)
        bubble_arr = best_case_arr.copy()
        bubble_time_best = timeit.timeit(lambda: bubble_sort(bubble_arr), number=1)
        bubble_sort_times_best.append(bubble_time_best)

        quick_arr = best_case_arr.copy()
        quick_time_best = timeit.timeit(lambda: quick_sort(quick_arr), number=1)
        quick_sort_times_best.append(quick_time_best)

    return sizes, bubble_sort_times_worst, quick_sort_times_worst, bubble_sort_times_best, quick_sort_times_best


def plot_performance(sizes, bubble_sort_times, quick_sort_times, title):
    plt.plot(sizes, bubble_sort_times, label='Bubble Sort')
    plt.plot(sizes, quick_sort_times, label='Quick Sort')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    sizes, bubble_sort_times, quick_sort_times, bubble_sort_times_best, quick_sort_times_best = test_sorting_algorithms()
    plot_performance(sizes, bubble_sort_times, quick_sort_times, 'Performance Comparison of Bubble Sort and Quick Sort (Average Case)')


