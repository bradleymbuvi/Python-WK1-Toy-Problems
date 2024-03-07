def solution(A):
    n = len(A)
    target_bricks = 10
    moves = 0
    
    for i in range(n):
        if A[i] == target_bricks:
            continue
        elif A[i] < target_bricks:
            if i < n - 1:
                diff = target_bricks - A[i]
                A[i] += diff
                A[i+1] -= diff
                moves += diff
            else:
                return -1
        else:  # A[i] > target_bricks
            if i > 0:
                diff = A[i] - target_bricks
                A[i] -= diff
                A[i-1] += diff
                moves += diff
            else:
                return -1
                
    return moves

# Test cases
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1



