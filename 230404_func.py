def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multiple(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else: # 0에 대한 예외처리
        return 0