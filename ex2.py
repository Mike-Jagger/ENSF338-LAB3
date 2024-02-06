import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def generate_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(algorithm, array):
    start_time = time.time()
    algorithm(array.copy())
    return time.time() - start_time

def main():
    # Small input sizes
    sizes = [1, 2, 5, 10, 20, 50, 100, 200, 300]

    # Large input sizes
    #sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

    bubble_times_best = []
    bubble_times_worst = []
    bubble_times_avg = []

    quicksort_times_best = []
    quicksort_times_worst = []
    quicksort_times_avg = []

    for size in sizes:
        # Best case for bubble sort: already sorted
        arr_best = list(range(1, size + 1))
        bubble_times_best.append(measure_time(bubble_sort, arr_best))

        # Worst case for bubble sort: sorted in reverse order
        arr_worst = list(range(size, 0, -1))
        bubble_times_worst.append(measure_time(bubble_sort, arr_worst))

        # Average case for bubble sort: random order
        arr_avg = generate_array(size)
        bubble_times_avg.append(measure_time(bubble_sort, arr_avg))

        # Best case for quicksort: pivot consistently divides the array into equal halves
        arr_best = list(range(1, size + 1))
        quicksort_times_best.append(measure_time(quicksort, arr_best))

        # Worst case for quicksort: pivot consistently divides the array into extremely uneven halves
        arr_worst = generate_array(size)
        quicksort_times_worst.append(measure_time(quicksort, arr_worst))

        # Average case for quicksort: random order
        arr_avg = generate_array(size)
        quicksort_times_avg.append(measure_time(quicksort, arr_avg))

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.plot(sizes, bubble_times_best, label='Bubble Sort (Best Case)')
    plt.plot(sizes, bubble_times_worst, label='Bubble Sort (Worst Case)')
    plt.plot(sizes, bubble_times_avg, label='Bubble Sort (Average Case)')

    plt.plot(sizes, quicksort_times_best, label='Quicksort (Best Case)')
    plt.plot(sizes, quicksort_times_worst, label='Quicksort (Worst Case)')
    plt.plot(sizes, quicksort_times_avg, label='Quicksort (Average Case)')

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Comparison of Bubble Sort and Quicksort')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
