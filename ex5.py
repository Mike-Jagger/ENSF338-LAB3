import time
import matplotlib.pyplot as plt
import numpy as np

# Task 1: Implement both traditional insertion sort and binary insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        low, high = 0, i - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1

        arr[low + 1:i + 1] = arr[low:i]
        arr[low] = key

# Task 2: Devise and run an experiment with increasing input lengths
def run_experiment(max_length):
    lengths = list(range(1, max_length + 1))
    insertion_times = []
    binary_insertion_times = []

    for length in lengths:
        avg_case_input = np.random.rand(length)

        # Measure time for traditional insertion sort
        start_time = time.time()
        insertion_sort(avg_case_input.copy())
        insertion_times.append(time.time() - start_time)

        # Measure time for binary insertion sort
        start_time = time.time()
        binary_insertion_sort(avg_case_input.copy())
        binary_insertion_times.append(time.time() - start_time)

    return lengths, insertion_times, binary_insertion_times

# Task 3: Plot the results of both algorithms
max_length = 1000  # You can adjust this based on your computational resources
lengths, insertion_times, binary_insertion_times = run_experiment(max_length)

plt.plot(lengths, insertion_times, label='Insertion Sort', marker='o')
plt.plot(lengths, binary_insertion_times, label='Binary Insertion Sort', marker='o')
plt.xlabel('Input Length')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Insertion Sort and Binary Insertion Sort')
plt.legend()
plt.show()

# Task 4: Discuss the results
"""
In the plot, we compare the performance of traditional insertion sort and binary insertion sort on average-case inputs
of increasing length. The x-axis represents the input length, and the y-axis represents the time taken to sort the array.

Observations:
- For smaller input lengths, both algorithms perform similarly.
- As the input length increases, binary insertion sort tends to outperform traditional insertion sort.
- Binary insertion sort has a time complexity of O(n^2) in the worst case, but it benefits from reduced constant
  factors due to the binary search for the insertion position.

Conclusion:
Binary insertion sort is generally faster for larger input sizes compared to traditional insertion sort in this average-case
scenario. However, the performance of these algorithms may vary based on the nature of the input data and specific
implementation details.
"""
