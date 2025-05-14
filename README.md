# DSA_with_Python

# 🧩 Python Competitive Programming Cheatsheet

## 🐍 Built-in Functions for CP

### 🔢 Numeric and Math Related
- `abs(x)` – Absolute value
- `pow(x, y, mod=None)` – Power (modular if mod given)
- `round(x)` – Rounding to nearest integer
- `max(iterable)`, `min(iterable)` – Max/min value
- `sum(iterable)` – Sum of elements
- `divmod(a, b)` – Returns `(a // b, a % b)`
- `bin(x)` – Binary representation
- `int(x)` – Convert to integer

### 🧰 Sequence / Iterable Related
- `len(iterable)` – Length
- `sorted(iterable, key=..., reverse=...)`
- `reversed(iterable)`
- `enumerate(iterable)` – Get index + value
- `zip(a, b)` – Pair elements
- `map(func, iterable)`
- `filter(func, iterable)`
- `any(iterable)` – Returns True if any element is True
- `all(iterable)` – Returns True if all elements are True

### 💬 String and I/O
- `input()` – Input from user
- `print()` – Output
- `str(x)` – Convert to string
- `format()` – String formatting

### 🎛 Others
- `type()` – Type of variable
- `range(start, stop, step)` – Generate numbers
- `set()`, `dict()`, `list()`, `tuple()` – Convert to respective types
- `eval()` – Evaluate string as expression (rarely used)

---

## 📚 Important Python Libraries for CP

### 📦 1. math – Math utilities
```python
import math
math.gcd(a, b)
math.sqrt(x)
math.factorial(n)
math.ceil(x), math.floor(x)
math.log(x, base)
```

### 📦 2. itertools – Combinatorics
```python
from itertools import permutations, combinations, product, combinations_with_replacement

permutations([1, 2])           # [(1, 2), (2, 1)]
combinations([1, 2, 3], 2)     # [(1, 2), (1, 3), (2, 3)]
product([0, 1], repeat=3)      # All binary strings of length 3
```

### 📦 3. collections – Advanced data structures
```python
from collections import Counter, defaultdict, deque

Counter([1, 2, 2])             # {1:1, 2:2}
defaultdict(int)              # Default value is 0
deque()                       # Fast append/pop from both ends
```

### 📦 4. heapq – Priority queue (min-heap)
```python
import heapq

heapq.heappush(heap, value)
heapq.heappop(heap)
heapq.heapify(arr)            # Convert list to heap
heapq.nlargest(k, iterable)   # k largest elements
```

### 📦 5. bisect – Binary search
```python
import bisect

bisect.bisect_left(arr, x)
bisect.bisect_right(arr, x)
bisect.insort(arr, x)         # Insert in sorted order
```

### 📦 6. functools – Higher-order functions
```python
from functools import reduce, lru_cache

reduce(lambda x, y: x + y, [1, 2, 3])
@lru_cache(maxsize=None)
def fib(n): ...
```

### 📦 7. sys – Fast I/O
```python
import sys

input = sys.stdin.readline   # Fast input
sys.setrecursionlimit(10**6) # Increase recursion depth
```

### 📦 8. string – Useful constants
```python
import string

string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
string.digits           # '0123456789'
```

---

## ✅ Optional / Advanced Libraries

| Library   | Use Case                                 |
|-----------|-------------------------------------------|
| `decimal` | High-precision decimal arithmetic         |
| `fractions` | Exact rational number calculations     |
| `random`  | Randomized algorithms (e.g., testing)     |
| `time`    | Profiling execution time                  |
| `numpy`   | Fast numerical operations (rare in CP)    |

---

## ⚡ Tips
- Use **PyPy** in online judges for faster runtime (same syntax as Python 3).
- Use `sys.stdin.readline()` for large inputs.
- Implement custom **SegmentTree**, **Union-Find**, **Trie**, etc., using classes.
- Avoid unnecessary imports in contests to reduce overhead.
