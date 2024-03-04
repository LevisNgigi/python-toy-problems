def solution(A):
    N = len(A)
    target = 10
    moves = 0
    
    # Calculate surplus/deficit of bricks for each box
    deficits = [0] * N
    for i in range(N):
        deficits[i] = A[i] - target
    
    # Iterate through boxes to move bricks
    for i in range(N - 1):
        if deficits[i] != 0:
            # Move excess bricks to the neighboring box
            if deficits[i] > 0:
                # Move to the right
                moves_to_right = min(deficits[i], deficits[i + 1])
                deficits[i] -= moves_to_right
                deficits[i + 1] -= moves_to_right
                moves += moves_to_right
            else:
                # Move to the left
                moves_to_left = min(abs(deficits[i]), abs(deficits[i + 1]))
                deficits[i] += moves_to_left
                deficits[i + 1] += moves_to_left
                moves += moves_to_left
    
    # Check if all boxes have 10 bricks
    for i in range(N):
        if deficits[i] != 0:
            return -1
    
    return moves

# Test cases
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1
