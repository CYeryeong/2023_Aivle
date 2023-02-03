# Q2 Answer template

def solution(numbers):
    sum = 45 
    #0부터 9까지의 합에서 numbers의 변수를 빼기
    for i in range(len(numbers)):
        sum -= numbers[i]
    return sum

numbers = [1,2,3,4,6,7,8,0]

answer = solution(numbers)
print(answer)