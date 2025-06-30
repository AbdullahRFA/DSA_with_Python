
def merge_array(left,right):
    i,j = 0,0
    n,m = len(left),len(right)
    result = []
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    # if i<n:
    #     while i<n:
    #         result.append(left[i])
    #         i+=1
    # elif j<m:
    #     while j<m:
    #         result.append(right[j])
    #         j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    n = len(arr)
    if n <=1:
        return arr
    mid = n//2
    left_array =arr[:mid]
    right_array = arr[mid:]
    left = merge_sort(left_array)
    right = merge_sort(right_array)
    return merge_array(left,right)

arr = list(map(int,input("Enter the array to be sorted: ").split()))
print("Sortd Array: ",merge_sort(arr))


"""

class Solution:
    def merge(self, arr, l, m, r):
        # Create temp arrays
        left = arr[l:m+1]
        right = arr[m+1:r+1]

        i = j = 0
        k = l

        # Merge temp arrays back into arr[l..r]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements of left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining elements of right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)
arr = [4, 1, 3, 9, 7]
sol = Solution()
sol.mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


"""