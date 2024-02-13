import numpy as np
import time
import matplotlib.pyplot as plt

def search_through_elements(dataset, target):
    for index in range(len(dataset)):
        if dataset[index] == target:
            return index
    return -1

def sort_via_quicksort(dataset):
    if len(dataset) <= 1:
        return dataset
    pivot = dataset[len(dataset) // 2]
    lesser_than_pivot = [elem for elem in dataset if elem < pivot]
    equal_to_pivot = [elem for elem in dataset if elem == pivot]
    greater_than_pivot = [elem for elem in dataset if elem > pivot]
    return sort_via_quicksort(lesser_than_pivot) + equal_to_pivot + sort_via_quicksort(greater_than_pivot)

def search_in_sorted(dataset, target):
    minimum = 0
    maximum = len(dataset) - 1
    while minimum <= maximum:
        middle = (minimum + maximum) // 2
        if dataset[middle] < target:
            minimum = middle + 1
        elif dataset[middle] > target:
            maximum = middle - 1
        else:
            return middle
    return -1

def evaluate_execution_time(search_method, dataset_size, repetitions=100):
    execution_times = []
    for _ in range(repetitions):
        dataset = np.arange(dataset_size, 0, -1)
        target_value = np.random.randint(1, dataset_size + 1)
        start = time.time()
        if search_method == "through_elements":
            search_through_elements(dataset, target_value)
        elif search_method == "sorted_search":
            sorted_dataset = sort_via_quicksort(dataset)
            search_in_sorted(sorted_dataset, target_value)
        finish = time.time()
        execution_times.append(finish - start)
    return np.mean(execution_times)

dataset_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

times_search_through_elements = [evaluate_execution_time("through_elements", size) for size in dataset_sizes]
times_sorted_search = [evaluate_execution_time("sorted_search", size) for size in dataset_sizes]

plt.figure(figsize=(10, 6))
plt.plot(dataset_sizes, times_search_through_elements, label='Linear searcg', marker='o')
plt.plot(dataset_sizes, times_sorted_search, label='Quicksort + Binary Search', marker='o')
plt.xlabel('Size of Dataset')
plt.ylabel('Mean Execution Time (seconds)')
plt.title('Comparative Analysis In WSC')
plt.legend()
plt.grid(True)
plt.savefig('search_methods_difficult_conditions.png')
plt.show()

#Observation:
#The algoritm efficiency is extremely high for quicksort + binary search in worst case scenario.
