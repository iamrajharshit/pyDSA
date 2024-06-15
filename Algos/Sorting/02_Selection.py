#selection sort
L1=[45,67,23,5,234,56,3]

def selection_sort(l1):
    
    for i in range(len(l1)):
        min_idx=i
        for j in range(i+1, len(l1)):
            if l1[min_idx]>l1[j]:
                min_idx=j

        l1[i],l1[min_idx]=l1[min_idx],l1[i]

    return l1

print(selection_sort(L1))