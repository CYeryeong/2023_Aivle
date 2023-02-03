# Q7 Answer Template

def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr.pop(i+1)
            print(arr)
    return answer

#arr = [1,1,3,3,0,1,1] # 이 Case는 성공
#arr = [4,4,4,3,3] # 실패
answer = solution(arr)
print(answer)