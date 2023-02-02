def solution(a, b):
    answer = -1
    for i in range(2, max(a,b)):
        if a%i == 0 and b%i == 0:
            answer = i
    return answer


c = solution(48, 54)
print(c)