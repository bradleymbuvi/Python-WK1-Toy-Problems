def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_len = len(alphabet)
    result = []
    
    for i in range(N):
        result.append(alphabet[i % alphabet_len])
    
    return ''.join(result)


# Test cases
print(solution(3))  # Output: "abc"

print(solution(5))  # Output: "abcde"