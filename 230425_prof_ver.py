def solution_2_java (arg):
    # 자바스러운 버전
    result = [0] * len(arg)
    for i in range(len(arg)):
        result[i] = arg[len(arg) -1 -i]
    return result

def solution_2 (arg):
    # 파이썬 스러운 버전 : 인덱스 !!!!
    return arg[::-1]

def solution_3 (arg):
    # 1에서 시작해서 3씩 커지는 등차수열의 일반항
    # An = 3n - 2
    sum = 0
    for i in range(1, arg+1): # 1부터 시작
        sum += 3 * i - 2
    return sum

def solution_4 (arg):
    min = len(arg)
    max = -1

    for num in arg:
        count = 0
        # 같은 숫자의 개수를 세는 코드
        for comp in arg:
            if num == comp:
                count += 1
        # print("{0}가 {1}개 있습니다".format(num, count))

        if count > max:
            max = count
        if count < min:
            min = count
        answer = max // min
    return answer

def solution_4_cntMethod (arg):
    count = 0
    min = len(arg)
    max = -1
    for num in arg:
        count = arg.count(num)
        if count > max:
            max = count
        if count < min:
            min = count
        answer = max // min
    return answer

if __name__ == '__main__':

    param = [2, 3, 3, 3, 1, 3, 3, 2, 3, 2]
    result4 = solution_4_cntMethod(param)
    print(result4)

    n = 5
    result3 = solution_3(n)
    print(result3)

    arr = [1, 4, 2, 3, 999]
    result2 = solution_2(arr)
    print(result2)



