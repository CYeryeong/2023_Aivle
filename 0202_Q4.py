data = input('숫자로 이루어진 문자열을 입력하세요. ')
total = 0
for i in range(len(data)):
    if int(data[i]) < 1 :
        total += int(data[i])
    else :
        if total == 0:
            total = int(data[i])
        elif total == 1:
            total = total + int(data[i])
        else :
            total = total*int(data[i])

print(total)