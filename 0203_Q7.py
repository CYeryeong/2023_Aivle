# Q7 Answer Template

def solution(arr):
    answer = []
    #while 문으로 앞과 뒤가 같으면 뒤를 삭제, 
    # 앞과 뒤가 다르면 뒤로 움직여 뒤와 뒤뒤비교 하면되지않을까
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr.pop(i+1)
            print(arr)
    return answer

#arr = [1,1,3,3,0,1,1] # 이 Case는 성공
#arr = [4,4,4,3,3] # 실패
answer = solution(arr)
print(answer)