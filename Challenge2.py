def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    sum_dict = {}
    max_sum = -1
    
    for num in A:
        s = digit_sum(num)
        if s in sum_dict:
            max_sum = max(max_sum, num + sum_dict[s])
            sum_dict[s] = max(sum_dict[s], num)
        else:
            sum_dict[s] = num
    
    return max_sum

# Test cases
print(solution([51, 71, 17, 42]))  # Output: 93
print(solution([42, 33, 60]))  # Output: 102
print(solution([51, 32, 43]))  # Output: -1



