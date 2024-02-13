import sys
sys.setrecursionlimit(20000)
import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]  # Elements less than pivot
        equal = [x for x in arr if x == pivot]   # Elements equal to pivot
        greater = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot
        return quicksort(less) + equal + quicksort(greater)


def measure_time(arr):
    """ Measure the time taken by quicksort to sort an array. """
    start_time = time.time()
    quicksort(arr)
    return time.time() - start_time

# Demonstration with a 16-element vector in worst-case scenario
worst_case_vector = list(range(16, 0, -1))
sorted_vector = quicksort(worst_case_vector)
print("Original vector:", worst_case_vector)
print("Sorted vector:", sorted_vector)

# Measuring quicksort performance on various input sizes
sizes = [10, 20, 50, 100, 200, 400, 800, 1600]
times = [measure_time(list(range(size, 0, -1))) for size in sizes]



# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, label='Quicksort Time', marker='o')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Performance on Worst-Case Inputs')
plt.legend()
plt.grid(True)

# Saving the plot
plt.savefig('4.4plt.png')  