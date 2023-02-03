a = list(input('리스트를 입력하여 주세요 : '))
key = input('찾을 인수를 입력하여 주세요 : ')

#이진 검색
def bin_search(a, key):
    pl = 0
    pr = len(a)-1
    print(a)
    while pl < pr:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
    return -1
        

index = bin_search(a, key)

if index == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 a[{index}]에 있습니다.')