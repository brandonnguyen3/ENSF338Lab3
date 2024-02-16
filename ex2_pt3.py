import time
import random
import matplotlib.pyplot as plt
import sys 
sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quicksort(arr, worst_case=False):
    if len(arr) <= 1:
        return arr
    
    if worst_case:
        pivot = arr[0]  # Choose the first element as the pivot
    else:
        pivot = arr[len(arr) // 2]  # Choose middle element as the pivot

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left, worst_case) + middle + quicksort(right, worst_case)

def choose_algorithm(size, bubble_threshold):
    if size <= bubble_threshold:
        return bubble_sort
    else:
        return quicksort

def generate_input_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def test_algorithm(algorithm, input_data):
    start_time = time.time()
    algorithm(input_data)
    end_time = time.time()
    return end_time - start_time

def run_tests(input_sizes, bubble_threshold):
    bubble_sort_best_times = []
    bubble_sort_worst_times = []
    bubble_sort_avg_times = []

    quicksort_best_times = []
    quicksort_worst_times = []
    quicksort_avg_times = []

    for size in input_sizes:
        input_data = generate_input_data(size)

        chosen_algorithm = choose_algorithm(size, bubble_threshold)

        

        # Worst case: reverse array for bubble sort, ascending array for quicksort
        if chosen_algorithm == bubble_sort:
            # Best case: sorted array
            bubble_sort_avg_times.append(test_algorithm(chosen_algorithm, input_data))
            bubble_sort_worst_times.append(test_algorithm(chosen_algorithm, sorted(input_data, reverse=True)))
            bubble_sort_best_times.append(test_algorithm(chosen_algorithm, sorted(input_data)))
            # Average case: random order
            
        else:
            quicksort_avg_times.append(test_algorithm(lambda x: chosen_algorithm(x, worst_case=True), sorted(input_data)))
            quicksort_worst_times.append(test_algorithm(lambda x: chosen_algorithm(x, worst_case=True), sorted(input_data, reverse=True)))
            quicksort_best_times.append(test_algorithm(chosen_algorithm, sorted(input_data)))

        quicksort_avg_times.append(test_algorithm(chosen_algorithm, input_data))

    return (bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times,
            quicksort_best_times, quicksort_worst_times, quicksort_avg_times)

def plot_performance(input_sizes, *times_sets):
    plt.figure(figsize=(10, 6))

    labels = ['Bubble Sort (Best)', 'Bubble Sort (Worst)', 'Bubble Sort (Avg)',
              'Quicksort (Best)', 'Quicksort (Worst)', 'Quicksort (Avg)']

    markers = ['o', 's', 'D', '^', 'v', '<']

    for i, times in enumerate(times_sets):
        plt.plot(input_sizes, times, label=labels[i], marker=markers[i])

    plt.xlabel('Input Size')
    plt.ylabel('Runtime (s)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.show()

def choose_threshold(input_sizes, bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times,
                     quicksort_best_times, quicksort_worst_times, quicksort_avg_times):
    # Analyze the performance plots to choose a threshold for each case
    # You might want to choose the point where the two algorithms cross over for each case

    best_threshold_index = next(
        i for i, (bubble_time, quicksort_time) in enumerate(zip(bubble_sort_best_times, quicksort_best_times))
        if quicksort_time < bubble_time
    )

    worst_threshold_index = next(
        i for i, (bubble_time, quicksort_time) in enumerate(zip(bubble_sort_worst_times, quicksort_worst_times))
        if quicksort_time < bubble_time
    )

    avg_threshold_index = next(
        i for i, (bubble_time, quicksort_time) in enumerate(zip(bubble_sort_avg_times, quicksort_avg_times))
        if quicksort_time < bubble_time
    )

    best_threshold_size = input_sizes[best_threshold_index]
    worst_threshold_size = input_sizes[worst_threshold_index]
    avg_threshold_size = input_sizes[avg_threshold_index]

    return best_threshold_size, worst_threshold_size, avg_threshold_size


if __name__ == "__main__":
    input_sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 7500, 10000]

    bubble_threshold = 200  # Adjust this threshold based on your analysis

    (bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times,
     quicksort_best_times, quicksort_worst_times, quicksort_avg_times) = run_tests(input_sizes, bubble_threshold)

    plot_performance(input_sizes,
                     bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times,
                     quicksort_best_times, quicksort_worst_times, quicksort_avg_times)
    
    best_threshold, worst_threshold, avg_threshold = choose_threshold(
        input_sizes,
        bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times,
        quicksort_best_times, quicksort_worst_times, quicksort_avg_times
    )

    print(f"Chosen threshold sizes - Best case: {best_threshold}, Worst case: {worst_threshold}, Avg case: {avg_threshold}")
