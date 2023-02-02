def solution(a, b):
    answer = -1
    
    for j in range(1, max(a,b), 1):
        for i in range(1, max(a,b), 1): 
            #for문 안에 for문을 넣고, range는 max에 맞추기
            if a*i == b*j :
                answer = a*i
                return answer
            else :
                continue           

c = solution(12, 24)
print(c)