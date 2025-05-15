
# ⚡ Kadane's Algorithm - Maximum Subarray Sum

Kadane's Algorithm is a famous dynamic programming technique used to find the **maximum sum of a contiguous subarray** in a 1D array of integers. It works in linear time and is highly efficient for this type of problem.

---

## 💡 What It Does

Given an array of integers (positive, negative, or zero), it finds the **maximum sum of any contiguous subarray** within it.

---

## ⚙️ How It Works

The algorithm maintains two variables:
- `current_sum`: maximum subarray sum ending at the current index
- `max_sum`: maximum subarray sum found so far

### 🔁 Logic:

- Iterate through the array.
- For each element `arr[i]`, update `current_sum` as:
  ```python
  current_sum = max(arr[i], current_sum + arr[i])
  ```
- Update `max_sum` as:
  ```python
  max_sum = max(max_sum, current_sum)
  ```

To also return the subarray, track indices using extra pointers:
- `start`, `end`, and `temp_start` to record the subarray boundaries.

---

## 🧠 When to Use It

- When you need to find the maximum profit/loss trend in stock prices.
- For solving dynamic programming problems involving ranges.
- During competitive programming and coding interviews.

---

## 📊 Time & Space Complexity

- **Time Complexity:** `O(n)` — Linear time.
- **Space Complexity:** `O(1)` — Only constant extra space is used.

---

## 👀 Visualization (Step-by-Step)

For array: `[2, 3, -8, 7, -1, 2, 3]`

| Index | Element | Current Sum | Max Sum | Subarray |
|-------|---------|-------------|---------|----------|
| 0     | 2       | 2           | 2       | [2]      |
| 1     | 3       | 5           | 5       | [2, 3]   |
| 2     | -8      | -3          | 5       | [2, 3]   |
| 3     | 7       | 7           | 7       | [7]      |
| 4     | -1      | 6           | 7       | [7]      |
| 5     | 2       | 8           | 8       | [7, -1, 2] |
| 6     | 3       | 11          | 11      | [7, -1, 2, 3] |

✅ Final Output: `11`, Subarray: `[7, -1, 2, 3]`

---

## 🧑‍💻 Python Code

```python
def kadane_algo(arr):
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, arr[start:end+1]
```

---

## 🏷️ Tags

`#KadaneAlgorithm` `#DynamicProgramming` `#Algorithms` `#Python` `#MaxSubarray` `#CodingInterview` `#ProblemSolving` `#TechTips`

---

💬 *Have you used Kadane’s Algorithm in your projects or interviews? Share your experiences below!*
