a, b = map(int, input('1 이상 1000 이하의 두 정수를 순서대로 입력해주세요 : ').split(','))
cnt, total = 0,0 
for i in range(a, b+1):
    for j in range(1, i+1):
        if i%j == 0:
            cnt += 1
        else :
            continue
        
    if cnt%2 == 0:
        total += i
    else :
        total -= i
    cnt = 0
    
print(total)