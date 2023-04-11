import matplotlib.pyplot as plt
import random as r
from sklearn.linear_model import LinearRegression

# y 함수
def true_func(x):
    return 2 * x + 3

if __name__ == "__main__":
    x_min = 1
    x_max = 50
    x = list(range(x_min, x_max)) # 1부터 49까지를 리스트에 담는다
    y = []
    x_2d = []
    y_true = []

    for i in x:
        x_2d.append([i]) # 대괄호를 쳐서 2차원..
        y_true.append(true_func(i))
        y.append(true_func(i) + r.randint(-10, 10)) # 노이즈 추가

    # 선형회귀모델 생성
    lr = LinearRegression() # 생성자 호출
    # lr.fit(x, y) # 데이터를 넣고 fit 해라 -> 에러. 데이터를 reshape해줘야함. 차원을 늘려달라고!
    lr.fit(x_2d, y)

    # predict
    # y_pred = lr.predict(x_2d)
    y_pred = lr.predict([[51], [52], [53], [54]])

    # plt.plot(x_2d, y_pred, "y-") # 갯수가 안맞아서 에러나는거
    # plt.plot(x_2d, y, "b+")
    # plt.plot(x_2d, y_pred, "r^")
    # plt.plot(x_2d, y_true, "go")
    plt.show()

