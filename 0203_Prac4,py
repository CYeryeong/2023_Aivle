a = list(map(int, input('리스트를 입력하여주세요 :').split()))
# input을 int로 받는 map을 한 후 list로 형변환해야함
maximum = a[0]

def search_max(a):
    global maximum
    for i in range(1, len(a)):
        if maximum < a[i]:
            maximum = a[i]
        else:
            continue

def maximum_index(maximum):
    for i in range(len(a)) :
        if a[i] == maximum:
            return i

maximum = search_max(a)
index = maximum_index(maximum)

print(f'최대값은 {maximum}이며, a[{index}]에 있습니다.')