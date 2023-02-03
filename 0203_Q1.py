# Q1 Answer template

def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    zero_cnt, same_num = 0, 0
    ranking = [6, 6, 5, 4, 3, 2, 1]

    #0의 개수 구하기
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero_cnt += 1
        else:
            continue

    #일치하는 숫자의 개수 구하기
    for i in range(zero_cnt-1, len(lottos)):
        for j in range(6):
            if lottos[i] == win_nums[j]:
                same_num += 1
            else :
                continue
        

    #최고 순위와 최저 순위 출력하기
    answer.append(ranking[same_num+zero_cnt])
    answer.append(ranking[zero_cnt])

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)