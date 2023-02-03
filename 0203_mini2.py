def reverse_list(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
        
print('리스트를 역순으로 출력합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

reverse_list(x)

print('리스트를 역순으로 출력합니다.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')
print(x)