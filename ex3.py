import numpy as np
import matplotlib.pyplot as plt

def custom_sort(arr):
    n = len(arr)
    num_comparisons = 0
    num_swaps = 0
    
    for i in range(n):
        for j in range(0, n-i-1):
            num_comparisons += 1  
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                num_swaps += 1
                
    return arr, num_comparisons, num_swaps

def perform_sorting_experiments(sizes):
    results = {
        'size': [],
        'comparisons': [],
        'swaps': []
    }
    
    for size in sizes:
        data = np.random.randint(0, 100, size)
        _, comparisons, swaps = custom_sort(data.copy())
        
        results['size'].append(size)
        results['comparisons'].append(comparisons)
        results['swaps'].append(swaps)
    
    return results

def visualize_results(results):
    sizes = results['size']
    comparisons = results['comparisons']
    swaps = results['swaps']

    plt.figure(figsize=(12, 6))
    plt.plot(sizes, comparisons, label='Comparisons', marker='o')
    plt.title('Number of Comparisons')
    plt.xlabel('Input Size')
    plt.ylabel('Number of Comparisons')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('custom_sort_comparisons.png')
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(sizes, swaps, label='Swaps', color='r', marker='o')
    plt.title('Number of Swaps')
    plt.xlabel('Input Size')
    plt.ylabel('Number of Swaps')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('custom_sort_swaps.png')
    plt.show()

if __name__ == "__main__":
    input_sizes = range(10, 101, 10)  
    results_data = perform_sorting_experiments(input_sizes)
    visualize_results(results_data)
