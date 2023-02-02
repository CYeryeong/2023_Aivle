data = input('숫자로 이루어진 문자열을 입력하세요. ')
total = 0
for i in range(len(data)):
    if data[i] == 0:
        total += 0
    elif data[i] != 0:
        if total == 0:
            total = 1
            total = total*int(data[i])
        else :
            total = total*int(data[i])
result = total

print(result)