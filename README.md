Prime Number Analyzer

Description

The Prime Number Analyzer is a Python-based project that checks whether a given number is prime and generates all prime numbers within a specified range. It uses functions, loops, conditional statements, and basic mathematical operations to perform prime number analysis efficiently.

Objectives

- To understand prime numbers and their properties.
- To practice Python functions, loops, and conditional statements.
- To generate prime numbers within a given range.
- To improve logical thinking and problem-solving skills.
- To learn basic algorithm optimization.

Features

- Checks whether a number is prime or not.
- Generates prime numbers within a specified range.
- Displays the total count of prime numbers found.
- Handles invalid choices and ranges.
- Uses a reusable "is_prime()" function.
- Optimizes prime checking by testing divisors only up to the square root of the number.

Technologies Used

- Programming Language: Python
- IDE: VS Code or IDLE

How to Run

1. Install Python on your computer.

2. Create a file named "prime_analyzer.py".

3. Copy the Python program into the file.

4. Open the terminal and navigate to the project folder.

5. Run the following command:
   
   "python3 prime_analyzer.py"

6. Choose an option from the menu.

7. Enter a number or a range to get the result.

Sample Output

===== PRIME NUMBER ANALYZER =====
1. Check whether a number is prime
2. Generate prime numbers in a range

Enter your choice (1 or 2): 2
Enter the starting number: 1
Enter the ending number: 20

Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19]
Total prime numbers: 8

Algorithm

1. Start the program.
2. Display the menu with two options.
3. Accept the user's choice.
4. If the user chooses option 1, accept a number and check whether it is prime.
5. If the user chooses option 2, accept the starting and ending numbers.
6. Check each number in the range using the prime-checking function.
7. Store and display all prime numbers found.
8. Display the total count and terminate the program.

Time Complexity

- Prime checking: O(√n)
- Prime number generation: Depends on the size of the range and the numbers being checked.

Conclusion

The Prime Number Analyzer demonstrates the use of Python programming concepts to solve a mathematical problem. It provides an easy way to identify prime numbers and generate them within a specified range. This project improves understanding of functions, loops, conditions, and algorithm efficiency.
