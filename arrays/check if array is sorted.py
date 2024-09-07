arr=[1,3,4,5,6]

def sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            continue

        else:
            return f"NO"

    return f"Yes"

print(sorted(arr))