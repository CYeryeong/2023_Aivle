a = [2, 5, 1, 3, 9, 6, 7]
sentinel_cnt, linear_cnt = 0,0

def seq_search_sentinel(b, key):
    a = b.copy()
    a.append(key)
    global sentinel_cnt
    #전역 변수 함수에 끌어오기
    i=0
    while True:
        sentinel_cnt += 1
        if a[i] == key:
            break
        i += 1
    
    sentinel_cnt += 1 
    if i == len(b) : 
        return -1 
    else : i

def seq_search(a, key):
    i = 0
    global linear_cnt 
    #전역 변수 함수에 끌어오기
    while True:
        linear_cnt += 1
        if i == len(a):
            return -1
        
        linear_cnt += 1
        if a[i] == key:
            return i
        
        i += 1

seq_search(a, 7)
seq_search_sentinel(a, 7)

print('보초법을 사용한 while문의 if문 횟수는 '+str(sentinel_cnt)+'입니다.')
print('보초법을 사용하지 않은 while문의 if문 횟수는 '+str(linear_cnt)+'입니다.')  