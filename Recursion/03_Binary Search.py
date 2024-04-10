def binary_search(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, high, target)
        else:
            return binary_search(arr, low, mid - 1, target)
    else:
        return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
print(binary_search(arr, 0, len(arr) - 1, target))  # Output: 3
