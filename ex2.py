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

def generate_input_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def test_algorithm(algorithm, input_data):
    start_time = time.time()
    algorithm(input_data)
    end_time = time.time()
    return end_time - start_time

def run_tests(input_sizes):
    bubble_sort_best_times = []
    bubble_sort_worst_times = []
    bubble_sort_avg_times = []

    quicksort_best_times = []
    quicksort_worst_times = []
    quicksort_avg_times = []

    for size in input_sizes:
        input_data = generate_input_data(size)
        #BUBBLE SORT
        # best case: sorted array
        bubble_sort_best_times.append(test_algorithm(bubble_sort, sorted(input_data)))

        # worst case: reverse array
        bubble_sort_worst_times.append(test_algorithm(bubble_sort, sorted(input_data, reverse=True)))

        # average case: random order
        bubble_sort_avg_times.append(test_algorithm(bubble_sort, input_data))

        #QUICKSORT
        # best case: sorted array
        quicksort_best_times.append(test_algorithm(quicksort, sorted(input_data)))

        # worst case: ascending array
        quicksort_worst_times.append(test_algorithm(lambda x: quicksort(x, worst_case=True), sorted(input_data, reverse=True)))

        # average case: random order
        quicksort_avg_times.append(test_algorithm(quicksort, input_data))


    return (bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times,
            quicksort_best_times, quicksort_worst_times, quicksort_avg_times)

#used chatgpt
def plot_performance_cases(input_sizes, *times_sets, case_labels):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))  # Changed to 1 row and 3 columns
    fig.suptitle('Sorting Algorithm Performance')

    markers = ['o', 's', 'D', '^', 'v', '<']
    colors = ['b', 'g', 'r', 'c', 'm', 'y']

    for i, ax in enumerate(axs):
        if i < len(times_sets):
            all_times = times_sets[i]
            for j, case_label in enumerate(case_labels):
                case_times = all_times[j] if j < len(all_times) else []  # Handle different sizes
                marker_index = i * len(case_labels) + j  
                color_index = i * len(case_labels) + j  
                ax.plot(input_sizes[:len(case_times)], case_times, label=f"{case_label}", marker=markers[marker_index], color=colors[color_index])

                # Set title based on the case
                if i == 0:
                    ax.set_title("Best Case")
                elif i == 1:
                    ax.set_title("Worst Case")
                elif i == 2:
                    ax.set_title("Average Case")
    
            ax.set(xlabel='Input Size', ylabel='Runtime (s)')
            ax.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def choose_threshold(input_sizes, bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times,
                     quicksort_best_times, quicksort_worst_times, quicksort_avg_times, small_array_threshold=100):
    # Analyze the performance plots to choose a threshold for each case
    # You might want to choose the point where the two algorithms cross over for each case

    # Find the index where Quick Sort surpasses Bubble Sort for the best case
    best_threshold_index = next(
        i for i, (bubble_time, quicksort_time) in enumerate(zip(bubble_sort_best_times, quicksort_best_times))
        if quicksort_time < bubble_time
    )

    # Find the index where Quick Sort surpasses Bubble Sort for the worst case
    worst_threshold_index = next(
        i for i, (bubble_time, quicksort_time) in enumerate(zip(bubble_sort_worst_times, quicksort_worst_times))
        if quicksort_time < bubble_time
    )

    # Find the index where Quick Sort surpasses Bubble Sort for the average case
    avg_threshold_index = next(
        i for i, (bubble_time, quicksort_time) in enumerate(zip(bubble_sort_avg_times, quicksort_avg_times))
        if quicksort_time < bubble_time
    )

    # Extract the input sizes at the determined threshold indices
    best_threshold_size = input_sizes[best_threshold_index]
    worst_threshold_size = input_sizes[worst_threshold_index]
    avg_threshold_size = input_sizes[avg_threshold_index]

    # Determine when to use Bubble Sort for small arrays
    use_bubble_sort_best = best_threshold_size <= small_array_threshold
    use_bubble_sort_worst = worst_threshold_size <= small_array_threshold
    use_bubble_sort_avg = avg_threshold_size <= small_array_threshold

    # Return the threshold input sizes and the decision to use Bubble Sort for small arrays
    return (best_threshold_size, use_bubble_sort_best), (worst_threshold_size, use_bubble_sort_worst), (avg_threshold_size, use_bubble_sort_avg)
#end of chagpt



if __name__ == "__main__":
    input_sizes = [10, 24, 50, 80, 100, 110, 160, 200, 250, 290, 303, 346, 390, 440, 500, 570, 590, 600, 658, 750]
    #input_sizes = [20, 30, 110, 120, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 10000]

    (bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times,
     quicksort_best_times, quicksort_worst_times, quicksort_avg_times) = run_tests(input_sizes)

    plot_performance_cases(input_sizes,
                       [bubble_sort_best_times, quicksort_best_times],
                       [bubble_sort_worst_times, quicksort_worst_times],
                       [bubble_sort_avg_times, quicksort_avg_times],
                       case_labels=['Bubble Sort', 'Quicksort'])
    
    best_threshold, worst_threshold, avg_threshold = choose_threshold(
        input_sizes,
        bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times,
        quicksort_best_times, quicksort_worst_times, quicksort_avg_times, small_array_threshold=100
    )

    print("Bubble Sort Times:")
    for size, best_time, worst_time, avg_time in zip(input_sizes, bubble_sort_best_times, bubble_sort_worst_times, bubble_sort_avg_times):
        print(f"Size: {size}, Best Time: {best_time:.6f}s, Worst Time: {worst_time:.6f}s, Avg Time: {avg_time:.6f}s")

    print("\nQuicksort Times:")
    for size, best_time, worst_time, avg_time in zip(input_sizes, quicksort_best_times, quicksort_worst_times, quicksort_avg_times):
        print(f"Size: {size}, Best Time: {best_time:.6f}s, Worst Time: {worst_time:.6f}s, Avg Time: {avg_time:.6f}s")


    print(f"Chosen threshold sizes:")
    print(f"- Best case: {best_threshold[0]}, Use Bubble Sort: {best_threshold[1]}")
    print(f"- Worst case: {worst_threshold[0]}, Use Bubble Sort: {worst_threshold[1]}")
    print(f"- Avg case: {avg_threshold[0]}, Use Bubble Sort: {avg_threshold[1]}")




