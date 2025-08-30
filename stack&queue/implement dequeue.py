from collections import deque

def demo_deque_operations():
    print("=== Deque Demonstration ===\n")
    
    # 1. Create an empty deque
    dq = deque()
    print("1. Empty Deque:", dq)

    # 2. Append to right (like normal queue enqueue)
    dq.append(10)
    dq.append(20)
    dq.append(30)
    print("2. After append (right):", dq)

    # 3. Append to left
    dq.appendleft(5)
    dq.appendleft(1)
    print("3. After appendleft:", dq)

    # 4. Pop from right
    right = dq.pop()
    print("4. Pop right:", right, "Deque now:", dq)

    # 5. Pop from left
    left = dq.popleft()
    print("5. Pop left:", left, "Deque now:", dq)

    # 6. Peek at both ends
    print("6. Peek left:", dq[0], "Peek right:", dq[-1])

    # 7. Extend deque at right
    dq.extend([40, 50, 60])
    print("7. After extend (right):", dq)

    # 8. Extend deque at left
    dq.extendleft([-1, -2, -3])
    print("8. After extendleft:", dq)

    # 9. Rotate deque (right shift)
    dq.rotate(2)
    print("9. After rotate(2):", dq)

    # 10. Rotate deque (left shift)
    dq.rotate(-3)
    print("10. After rotate(-3):", dq)

    # 11. Insert at specific index
    dq.insert(2, 999)
    print("11. After insert at index 2:", dq)

    # 12. Remove first occurrence of value
    dq.remove(999)
    print("12. After remove(999):", dq)
    

    # 13. Count occurrences of element
    dq.append(20)
    print("13. Count of 20:", dq.count(20), "Deque:", dq)

    # 14. Reverse deque
    dq.reverse()
    print("14. After reverse:", dq)

    # 15. Maxlen (bounded deque)
    dq2 = deque(maxlen=5)
    dq2.extend([1, 2, 3, 4, 5])
    print("15. Fixed size deque:", dq2)
    dq2.append(6)  # pushes out leftmost
    print("   After append beyond maxlen:", dq2)

    print("16. Iterating through deque:")
    for x in dq:
        print("   Element:", x)
    
    # 16. Clear deque
    dq.clear()
    print("17. After clear:", dq)

if __name__ == "__main__":
    demo_deque_operations()
    