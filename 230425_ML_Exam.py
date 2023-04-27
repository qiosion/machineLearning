def solution_1(shirt_size):
    result = [0, 0, 0, 0, 0, 0]
    # XS S M L XL XXL
    for i in shirt_size:
        if i == "XS":
            result[0] += 1
        elif i == "S":
            result[1] += 1
        elif i == "M":
            result[2] += 1
        elif i == "L":
            result[3] += 1
        elif i == "XL":
            result[4] += 1
        elif i == "XXL":
            result[5] += 1
        else:
            print("잘못된 입력값")
    return result


def solution_2(arr):
    result = []
    length = len(arr)
    for i in range(0, length):
        result.append(arr[length - i - 1])
    return result


def solution_3(n):
    result = 0
    test = 1
    for i in range(0, n):
        test = (3 * i) + 1
        result += test
    return result


def solution_4(param):
    result = 0
    length = len(param)
    max = 0
    min = length
    for i in range(0, length):
        cnt = 0
        for j in range(0, length):
            if param[i] == param[j]:
                cnt += 1
        if max < cnt:
            max = cnt
        if min > cnt:
            min = cnt
    print("max : ", max, ", min : ", min)
    result = int(max / min)
    return result


if __name__ == '__main__':

    shirt_size = ["XL", "XXL", "XS", "XS", "XS"]
    result1 = solution_1(shirt_size)
    print(result1)

    arr = [1, 4, 2, 3, 999]
    result2 = solution_2(arr)
    print(result2)

    n = 5
    result3 = solution_3(n)
    print(result3)

    param = [2, 3, 3, 3, 1, 3, 3, 2, 3, 2]
    result4 = solution_4(param)
    print(result4)