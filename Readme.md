# Week one Python toy problems

# Minimum Moves to Distribute Bricks Challenge - Challenge_1.py

## Problem Description
There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks. In one move, you can take one brick from some box and move it to a box next to it (on the left or on the right). The goal is to find the minimum number of moves needed to end up with exactly 10 bricks in every box.

## Function Signature
```python
def solution(A):
    # Implementation goes here
```

## Input
- A: An array of N integers, where A[K] represents the number of bricks in the K-th box (1 ≤ N ≤ 100, 0 ≤ A[K] ≤ 100).

## Output
- Returns the minimum number of moves needed to end up with exactly 10 bricks in every box.
- If it is not possible to achieve the target configuration, the function returns -1.

## Examples
1. For `A = [7, 15, 10, 8]`, the function should return 7. You can perform the following sequence of moves:
   - Move three bricks from box number 1 to the box on the left: [10, 12, 10, 8];
   - Move two bricks from box number 1 to the box on the right: [10, 10, 12, 8];
   - Finally, move two bricks from box number 2 to the last box: [10, 10, 10, 10].

2. For `A = [11, 10, 8, 12, 8, 10, 11]`, the function should return 6. You can perform the following sequence of moves:
    - Move a brick from box number 0 to box number 2 (using two moves);
    - Move a brick from the last box two positions to the left (using two moves);
    - Move a brick from the middle box to each of its neighbors (another two moves).

3. For `A = [7, 14, 10]`, the function should return -1. It is not possible to end up with exactly 10 bricks in each box.

## Usage
```python
print(solution([19, 2]))  # Output: -1
print(solution([19, 1]))  # Output: 9
print(solution([21, 2, 7]))  # Output: 11
```


# Maximum Digit Sum Pair - challenge_2.py

This Python code provides a solution to the following problem:

## Problem Statement:

You are given an array `A` consisting of `N` integers. The task is to find the maximum sum of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum, the function returns -1.

## Function Signature:

```python
def solution(A):
    """
    Given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum.
    If there are no two numbers whose digits have an equal sum, the function returns -1.
    
    Parameters:
    - A: List[int] - The input array of integers.

    Returns:
    - int: The maximum sum of two numbers with equal digit sums, or -1 if no such pair exists.
    """
    # Implementation goes here

# Examples
print(solution([51, 71, 17, 42]))  # Output: 93
print(solution([42, 33, 60]))       # Output: 102
print(solution([51, 32, 43]))       # Output: -1
```

## Approach:

The algorithm uses a dictionary (`digit_sum_dict`) to store numbers based on their digit sums. It iterates through the array, calculates the digit sum for each number, and checks if there's a number with the same digit sum in the dictionary. If found, it updates the maximum sum if needed. Finally, the function returns the maximum sum.

## Examples:

1. For `A = [51, 71, 17, 42]`, the function should return `93`. There are two pairs of numbers whose digits add up to an equal sum: `(51, 42)` and `(17, 71)`. The first pair sums up to `93`.

2. For `A = [42, 33, 60]`, the function should return `102`. The digits of all numbers in `A` add up to the same sum, and choosing to add `42` and `60` gives the result `102`.

3. For `A = [51, 32, 43]`, the function should return `-1` since all numbers in `A` have digits that add up to different, unique sums.


# Solution for Creating a String with Equal Occurrences of Letters - challenge_3.py

The `solution` function takes an integer `N` as input and returns a string of length `N` containing as many different lowercase letters ('a'-'z') as possible, in which each letter occurs an equal number of times.

## Algorithm Explanation

1. Iterate through the alphabet ('a' to 'z') using ASCII values.
2. Calculate the number of occurrences for each letter based on the desired length `N`.
3. Repeat each letter the calculated number of occurrences and concatenate it to the result string.
4. Trim the result string to the desired length `N`.
5. Return the resulting string.

## Example Usage

```python
# Examples
print(solution(3))   # Output: "abc"
print(solution(5))   # Output: "abcde"
print(solution(30))  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"
```

## Additional Notes

- The solution ensures that each letter occurs an equal number of times in the resulting string, meeting the specified requirements.
- The algorithm has a time complexity of O(26) since it iterates through the 26 letters of the alphabet. The constant factor is relatively small, making it efficient for the given constraints (N is an integer within the range [1..200,000]).
- Feel free to adjust the code as needed for integration into your project.

## Authors :black_nib:
- **Levis Ngigi** <[LevisNgigi](https://github.com/LevisNgigi)>

# License

This project is licensed under the [MIT License](LICENSE)