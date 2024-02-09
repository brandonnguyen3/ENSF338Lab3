import json
import time

def read_sorted_array(filename):
    with open(filename, 'r') as file:
        sorted_array = json.load(file)
    return sorted_array

def read_search_tasks(filename):
    with open(filename, 'r') as file:
        search_tasks = json.load(file)
    return search_tasks

def binary_search(arr, target, start_midpoint):
    low = 0
    high = len(arr) - 1
    mid = start_midpoint
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    
    return -1

def time_search_task(arr, target, start_midpoint):
    start_time = time.time()
    result = binary_search(arr, target, start_midpoint)
    end_time = time.time()
    return result, end_time - start_time

def run_search_tasks(arr, search_tasks):
    results = {}
    for task in search_tasks:
        target = task['target']
        midpoints = task['midpoints']
        task_results = {}
        for midpoint in midpoints:
            result, time_taken = time_search_task(arr, target, midpoint)
            task_results[midpoint] = {'result': result, 'time': time_taken}
        results[target] = task_results
    return results

def visualize_results(results):
    for target, task_results in results.items():
        print(f"Results for target {target}:")
        for midpoint, data in task_results.items():
            print(f"Midpoint {midpoint}: Result = {data['result']}, Time taken = {data['time']} seconds")
        print()

def main():
    sorted_array = read_sorted_array('ex7data.json')
    search_tasks = read_search_tasks('ex7tasks.json')
    results = run_search_tasks(sorted_array, search_tasks)
    visualize_results(results)

if __name__ == "__main__":
    main()

