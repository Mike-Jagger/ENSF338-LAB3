import sys
sys.setrecursionlimit(20000)

def merge(arr, low, mid, high):
    # Create temporary arrays for left and right halves
    L = arr[low:mid+1]
    R = arr[mid+1:high+1]

    # Initial indexes for left, right and merged subarrays
    i = 0
    j = 0
    k = low

    # Merge the temp arrays back into arr[low:high+1]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Check if any elements were left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

# Example usage
arr = [8, 42, 25, 3, 3, 2, 27, 3]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
