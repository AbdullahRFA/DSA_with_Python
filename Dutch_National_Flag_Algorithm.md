
# 🇳🇱 Dutch National Flag Algorithm

🔵🔴⚪ **Understanding the Dutch National Flag Algorithm**  
_Sort an Array of 0s, 1s, and 2s in One Pass Efficiently!_

---

🚩 The **Dutch National Flag Algorithm**, proposed by **Edsger Dijkstra**, is a classic and efficient algorithm for sorting an array that contains only **three distinct values** — typically `0`, `1`, and `2`. The algorithm is particularly useful in problems like sorting colors, flags, or buckets.

---

## 💡 What It Does

It **sorts the array in-place** so that all 0s appear first, then 1s, and then 2s — in just a **single traversal** without using extra space.

---

## ⚙️ How It Works

The algorithm uses **three pointers**:

- `low`: Points to the boundary of the 0s region.  
- `mid`: Traverses the array and checks elements.  
- `high`: Points to the boundary of the 2s region.

### 🔁 Logic

- If `arr[mid] == 0`: Swap with `arr[low]`, increment both `low` and `mid`.
- If `arr[mid] == 1`: Just move `mid` forward.
- If `arr[mid] == 2`: Swap with `arr[high]`, decrement `high` (don’t increment `mid` yet!).

---

## 📊 Time & Space Complexity

- **🕒 Time Complexity**: `O(n)` → Each element is processed only once.  
- **💾 Space Complexity**: `O(1)` → No extra data structures used.

---

## 👀 Visualization

Initial array: `[2, 0, 1, 2, 1, 0]`

### Step-by-step swaps:

1. mid=0 → `arr[mid]=2`, swap with `high=5` → `[0, 0, 1, 2, 1, 2]`
2. mid=0 → `arr[mid]=0`, swap with `low=0` → `[0, 0, 1, 2, 1, 2]`
3. mid=1 → `arr[mid]=0`, swap with `low=1` → `[0, 0, 1, 2, 1, 2]`
4. mid=2 → `arr[mid]=1` → move forward
5. mid=3 → `arr[mid]=2`, swap with `high=4` → `[0, 0, 1, 1, 2, 2]`
6. mid=3 → `arr[mid]=1` → move forward

### Final Array: `[0, 0, 1, 1, 2, 2]`

All in one pass. No sorting function. No extra array. Just smart pointer movement! ✅

---
```python
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        n = len(arr)-1
        low,mid,high = 0,0,n
        while mid <= high:
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid],arr[high] = arr[high],arr[mid]
                high -= 1

```

## 🚀 When to Use This Algorithm?

- When you're dealing with only **three distinct values** (like RGB colors, binary states, flags, etc.)
- When you need a highly optimized **in-place sort**
- For solving **interview problems** efficiently (very popular in coding interviews!)

---

## 💬 Let's Discuss!

Have you implemented this algorithm before? Drop your thoughts, variations, or code snippets below! 👇

---

### 📌 Tags
`#Algorithms` `#Python` `#DataStructures` `#SortingAlgorithm` `#CodingInterview` `#LinkedInLearning` `#SoftwareEngineering` `#TechTips` `#DutchNationalFlag` `#InPlaceSorting` `#ProblemSolving` `#ProgrammingTips`
