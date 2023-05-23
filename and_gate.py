

# step function 계단함수 구현
def activation_func(x):
    if x <= 0:
        return 0
    else:
        return 1

# AND 게이트 신경망 구현
def AND_gate(x1, x2):
    w1 = 0.4
    w2 = 0.2
    b = -0.5

    w_sum = w1 * x1 + w2 * x2 + b

    return activation_func(w_sum)


if __name__ == "__main__":
    # print(activation_func(0.1)) # 1
    print(AND_gate(0, 0)) # 0
    print(AND_gate(0, 1)) # 0
    print(AND_gate(1, 0)) # 0
    print(AND_gate(1, 1)) # 1