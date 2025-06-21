"""Selection Sort"""
"""
⸻
✅ Selection Sort Technique

🔧 How it works:

Selection Sort is a comparison-based sorting algorithm that divides the array into two parts:
	•	Sorted part (starting empty)
	•	Unsorted part

At each step:
	1.	The algorithm finds the minimum element in the unsorted part.
	2.	It swaps that element with the first unsorted element.
	3.	It then shrinks the unsorted part and expands the sorted part by one element.
⸻
📥 Input:

arr = [2, 6, 4, 5, 9, 1, 2, 3]

🧠 Algorithm:

At each step, find the smallest element in the unsorted part and swap it with the element at the current index.

⸻

🔄 Step-by-Step Trace:

Pass	Index i	    Unsorted Part	        Min Element     &   Index	Swap With	    Array After Swap
1	    0	    [2, 6, 4, 5, 9, 1, 2, 3]	1 at index 5	            arr[0]	        [1, 6, 4, 5, 9, 2, 2, 3]
2	    1	    [6, 4, 5, 9, 2, 2, 3]	    2 at index 5	            arr[1]	        [1, 2, 4, 5, 9, 6, 2, 3]
3	    2	    [4, 5, 9, 6, 2, 3]	        2 at index 6	            arr[2]	        [1, 2, 2, 5, 9, 6, 4, 3]
4	    3	    [5, 9, 6, 4, 3]	            3 at index 7	            arr[3]	        [1, 2, 2, 3, 9, 6, 4, 5]
5	    4	    [9, 6, 4, 5]	            4 at index 6	            arr[4]	        [1, 2, 2, 3, 4, 6, 9, 5]
6	    5	    [6, 9, 5]	                5 at index 7	            arr[5]	        [1, 2, 2, 3, 4, 5, 9, 6]
7	    6	    [9, 6]	                    6 at index 7	            arr[6]	        [1, 2, 2, 3, 4, 5, 6, 9]
8	    7	    [9]	                        Already sorted	            –	            [1, 2, 2, 3, 4, 5, 6, 9] ✅ Sorted!


⸻

✅ Final Sorted Array:

[1, 2, 2, 3, 4, 5, 6, 9]


⸻

🔍 Key Notes:
	•	At each pass, the smallest element from the remaining unsorted part is selected.
	•	Then it’s swapped into the correct place.
	•	Selection sort does not adapt — it performs the same number of comparisons even if the array is partially sorted.

⸻

⏱️ Time Complexity

Case	            Time	        Why
Best Case	        O(n²)	    Even if already sorted, it still compares every pair
Average Case	    O(n²)	    Two nested loops — one to select, one to find minimum
Worst Case	        O(n²)	    Always performs same number of comparisons regardless of input

	•	Outer loop runs n times
	•	Inner loop runs on average n/2 times per outer iteration
→ Total comparisons ≈ n * (n-1)/2 → O(n²)

⸻

📦 Space Complexity

Space	Complexity	Why
Auxiliary	O(1)	No extra space is used — sorting is in-place


⸻

📌 Summary

Feature	                    Value
Algorithm Type	            Comparison-based
Time Complexity	            O(n²)
Space Complexity	        O(1)
Stable Sort	                ❌ No (unless modified)
In-place	                ✅ Yes
Best For	                Small datasets, simple logic


⸻

🔍 Why O(n²) and O(1)?
	•	O(n²): Because it always does two nested loops (n * n-1) regardless of the order of input.
	•	O(1): Because it doesn’t use any extra array or data structure — it just swaps in the original list.

"""
def selection_sort_for_ascending_order(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

def selection_sort_for_descending_order(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i+1,n):
            if arr[max_index]<arr[j]:
                max_index = j
        arr[i],arr[max_index] = arr[max_index],arr[i]


arr = [2,6,4,5,9,1,2,3]
print("Before Sorting: ",arr)
selection_sort_for_ascending_order(arr)
print("After Sorting(ascending order): ",arr)
selection_sort_for_descending_order(arr)
print("After sorting(Descending order): ",arr)


