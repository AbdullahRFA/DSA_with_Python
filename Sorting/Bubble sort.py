def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        is_swap = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swap = True
        if not is_swap:
            break

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        is_swap = False
        for j in range(0, n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swap = True
        if not is_swap:
            break

# Main logic
arr = list(map(int, input("Enter space-separated integers: ").split()))
print("Before sort:", arr)

arr_asc = arr.copy()
bubble_sort_asc(arr_asc)
print("After ascending sort:", arr_asc)

arr_desc = arr.copy()
bubble_sort_desc(arr_desc)
print("After descending sort:", arr_desc)