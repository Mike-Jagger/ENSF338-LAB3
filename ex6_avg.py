import numpy as np
import time
import matplotlib.pyplot as plt

# Searching an item linearly
def search_linearly(sequence, target):
    for position in range(len(sequence)):
        if sequence[position] == target:
            return position
    return -1

# Executing binary search on a sorted array
def search_binary(sequence, target):
    start = 0
    end = len(sequence) - 1

    while start <= end:
        middle = (start + end) // 2

        if sequence[middle] < target:
            start = middle + 1
        elif sequence[middle] > target:
            end = middle - 1
        else:
            return middle
    return -1

# Sorting an array using the quicksort algorithm
def sort_quicksort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence[len(sequence) // 2]
        lesser = [item for item in sequence if item < pivot]
        equal = [item for item in sequence if item == pivot]
        greater = [item for item in sequence if item > pivot]
        return sort_quicksort(lesser) + equal + sort_quicksort(greater)

# Tracking execution time for each search strategy
dataset_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
times_for_linear_search = []
times_for_binary_search = []

for size in dataset_sizes:
    time_linear = 0
    time_binary = 0
    for _ in range(100):
        data = np.random.randint(1, 100, size)
        search_value = np.random.randint(1, 100)
        
        start = time.time()
        search_linearly(data, search_value)
        time_linear += (time.time() - start)
        
        sorted_data = sort_quicksort(data)
        start = time.time()
        search_binary(sorted_data, search_value)
        time_binary += (time.time() - start)
        
    times_for_linear_search.append(time_linear / 100)
    times_for_binary_search.append(time_binary / 100)

plt.figure(figsize=(10, 5))
plt.plot(dataset_sizes, times_for_linear_search, label='Linear Search', marker='o')
plt.plot(dataset_sizes, times_for_binary_search, label='Quicksort + Binary Search', marker='x')
plt.xlabel('Dataset Size')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Comparing Efficiency of Search Strategies')
plt.legend()
plt.grid(True)
plt.savefig("search_algorithm_performance.png")  # Storing the comparison graph
plt.show()

# Q4

# - Larger datasets has more efficiency using quick-sort and using binary search compared to linear search.
# - Smaller datasets has a less difference in efficiency for both search strategies.
