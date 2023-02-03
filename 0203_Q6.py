# Q6 Answer template

def solution(arr):
    b = list(arr)
    # list를 다른 변수에 또다른 list로 만들고 싶으면
    # list 선언을 통해 새로운 list임을 알려야한다.
    b.sort()
    arr.remove(b[0])

    if len(arr) == 0:
        arr = [-1]
    
    return arr


arr = [5, 4, 2, 6, 7]
answer = solution(arr)
print(answer)