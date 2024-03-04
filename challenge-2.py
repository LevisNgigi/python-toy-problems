def digit_sum(number):
    # Function to calculate the sum of digits of a number
    return sum(int(digit) for digit in str(number))

def solution(A):
    max_sum = -1
    sum_dict = {}

    # Iterate through the array and calculate the digit sum for each number
    for number in A:
        digit_sum_value = digit_sum(number)
        if digit_sum_value in sum_dict:
            # If a number with the same digit sum exists, update max_sum if needed
            max_sum = max(max_sum, number + sum_dict[digit_sum_value])
            # Update the maximum number encountered so far with the same digit sum
            sum_dict[digit_sum_value] = max(number, sum_dict[digit_sum_value])
        else:
            # Store the number with its digit sum for future reference
            sum_dict[digit_sum_value] = number
    
    return max_sum

# Test cases
print(solution([51, 71, 17, 42]))  # Output: 93
print(solution([42, 33, 60]))  # Output: 102
print(solution([51, 32, 43]))  # Output: -1
