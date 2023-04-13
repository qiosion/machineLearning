import matplotlib.pyplot as plt
import random as r
from sklearn.linear_model import LinearRegression # 선형회귀
import math
import numpy as np
from sklearn.preprocessing import PolynomialFeatures # 다중회귀

if __name__ == "__main__":
    # for i in range(100):
    #     x = 6 * np.random.random() - 3
    #     print(x)

    # 넘파이를 사용하면 for문 안돌려도 된다
    # x = np.random.rand(100)
    # print(x)

    # # -3 ~ 3 까지의 난수 100개 만들고 싶다
    # n = 100
    # x = 6 * np.random.rand(n, 1) -3
    # # 이때 1은 1차원 배열로 감싸서 만들고 싶다는 말 -> x 자체는 2차원이 됨
    #
    # y = 0.5 * x ** 2 + x + 2 + np.random.rand(n, 1)
    # # np.random.ran(n, 1)는 노이즈를 준 것
    #
    # plt.scatter(x, y, s=3) # 기본사이즈 5, 사이즈를 3으로 설정
    # # plt.show()

    # 다항회귀를 하는 방법
    # -3 ~ 3 까지의 난수 100개 만들고 싶다
    n = 100
    x = np.linspace(0, 2 * math.pi, 12)
    x = x.reshape(-1, 1)
    y = np.sin(x)
    plt.scatter(x, y)

    # x의 차수를 늘려야 한다
    pf = PolynomialFeatures(degree=3) # 2차식
    x_poly = pf.fit_transform(x)
    # print(x_poly)

    # 늘어난 차수의 x를 가지고 선형회귀한다
    lr = LinearRegression()
    lr.fit(x_poly, y)

    # 학습이 끝났으니 예측해본다
    y_pred = lr.predict(x_poly)
    plt.scatter(x, y_pred)
    plt.show()

    # # 균일분포
    # x = np.random.uniform(-3, 3, 1000)
    # plt.hist(x)
    # plt.show()
    #
    # # 정규분포
    # y = np.random.normal(-3, 3, 1000)
    # plt.hist(y)
    # plt.show()