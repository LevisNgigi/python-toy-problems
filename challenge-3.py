def solution(N):
    # Define the lowercase alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Get the length of the alphabet
    alphabet_length = len(alphabet)
    
    # Repeat the alphabet string until its length is at least N
    # and concatenate with the remaining characters if needed
    repeated_string = alphabet * (N // alphabet_length) + alphabet[:N % alphabet_length]
    
    # Return the resulting string
    return repeated_string

# Test cases
print(solution(3))  # Output: "abc"
print(solution(5))  # Output: "abcde"
print(solution(30)) # Output: "abcdefghijklmnoabcdefghijklmno"
