a = []
i = 2
while i <=1000:
    answer = 0
    j = 2
    
    while j <= i : #j는 2부터 i까지 올라가기
        if i//j == 0 and j < i:
            answer = -1
            break
        j += 1
    
    if answer != -1 :
        a.append(i)
    
    i += 1


print(a)
