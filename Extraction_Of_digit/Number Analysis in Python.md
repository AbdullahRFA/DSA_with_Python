Here’s a complete README.md file that clearly explains all the topics and code functionalities from your Python script:

⸻

📘 README.md

🧮 Number Analysis with Python

This project demonstrates a few basic yet important concepts in number theory using Python. The code provides functionality to:
	•	Count the number of digits in a number
	•	Reverse a number
	•	Check whether a number is a palindrome
	•	Check whether a number is an Armstrong number

⸻

📌 Features and Concepts

1. Counting the Number of Digits

This section asks the user to input a number and counts how many digits it contains by continuously dividing the number by 10.

num = int(input("Enter a number to count its number of digits: "))
cnt = 0
tem = num
while num != 0:
    num //= 10
    cnt += 1
print(f"Number of digit in {tem} is ", cnt)

	•	Concept: Integer division (//) removes the last digit of a number.
	•	Use case: Helpful in numeric analysis, digit-based algorithms, and validation logic.

⸻

2. Reversing a Number

This portion reverses the digits of a number.

num = int(input("Enter a number to reverse: "))
tem = num
reversed_num = 0
while num != 0:
    r = num % 10
    reversed_num = reversed_num * 10 + r
    num //= 10
print(f"Reverse of {tem} is ", reversed_num)

	•	Concept: Extracting digits with %, and building the reverse by multiplying previous result by 10.
	•	Example: 123 → 321

⸻

3. Palindrome Number Check

A palindrome number reads the same backward as forward.

num = int(input("Enter a number to check palindrome: "))
tem = num
reversed_num = 0
while num != 0:
    r = num % 10
    reversed_num = reversed_num * 10 + r
    num //= 10
if tem == reversed_num:
    print(f"{tem} is a palindrome number")
else:
    print(f"{tem} is not a palindrome number")

	•	Concept: Reverse the number and compare it with the original.
	•	Example: 121, 1331 → Palindrome ✅

⸻

4. Armstrong Number Check

An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

Example:
	•	153 → 1³ + 5³ + 3³ = 153
	•	9474 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474

def count_of_digit(n):
    num = n
    cnt = 0
    while num != 0:
        num //= 10
        cnt += 1
    return cnt

def check_armstrong(n, cnt):
    num = n
    armstrong_number = 0
    while num != 0:
        r = num % 10
        armstrong_number += r ** cnt
        num //= 10
    return n == armstrong_number

n = int(input("Enter a number to check if it is an Armstrong number or not: "))
cnt = count_of_digit(n)
if check_armstrong(n, cnt):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

	•	Concept: Raise each digit to the power of total digits and sum them.
	•	Efficient Use of Functions: The logic is modularized with functions for better readability and reuse.

⸻

✅ Requirements
	•	Python 3.x
	•	No external libraries required

⸻

🚀 How to Run

Simply run the Python file in a terminal:

python filename.py

You will be prompted to enter a number for each operation.

⸻

📚 Summary

Feature	Description
Digit Counter	Counts total digits in a number
Reverser	Reverses a number
Palindrome Checker	Checks if number is same forward & backward
Armstrong Checker	Validates if a number is an Armstrong number


⸻

🧠 Topics Covered
	•	Looping (while)
	•	Conditional logic (if-else)
	•	Arithmetic operations (%, //, **)
	•	String formatting using f-strings
	•	Functions and modularity in Python

⸻
