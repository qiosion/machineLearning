import matplotlib.pyplot as plt
import random as r
from sklearn.linear_model import LinearRegression
import math
import numpy as np

if __name__ == "__main__":
    # a = np.array([1, 2, 3, 4]) # np 형태의 배열로 바꿔줌. 콤마 없음
    # print(a)
    # b = np.arange(10)
    # print(b)
    # c = np.linspace(-3.14, 3.14, 10) # linear spacee. -3.14부터 3.14부터 10개로 쪼개서 만들어줘
    # print(c)
    # d = np.reshape(-1, 1) # -1 전체 다를 한차원 변경???? 무슨말이야
    # print(d)

    # x = []
    # y = []

    # for i in range (0, 361, 30): # 0부터 360까지 30 간격으로
    #     # print(i)
    #     # i 는 각도 º --> 라디안 radian으로 바꾸고 싶다 --> 원주율(파이)이 필요함
    #     rad = i * math.pi / 180
    #
    #     sin_rad = math.sin(rad)
    #     # print(sin_rad)
    #
    #     # 데이터 reshape 위해 2차원 리스트로 만든다. 기존의 리스트에 한번 더 리스트로 넣어줌
    #     x.append([rad]) # x 리스트에 rad 라디안을 리스트로 넣음
    #     y.append([sin_rad]) # y 리스트에 사인(라디안)을 리스트로 넣음

    # numpy 넘파이 사용
    x = np.linspace(0, 2 * math.pi, 12) # 0부터 2파이(360도)까지를 12개로 쪼갬
    x = x.reshape(-1, 1) # x를 2차원으로 만듦
    y = np.sin(x)

    plt.scatter(x, y)
    # plt.show()

    # 학습을 하자 : fit
    # 이걸 선형함수 linear regression으로 만들면 가장 오차가 적은 일차함수를 그린다
    lr = LinearRegression()
    lr.fit(x, y)

    # 예측을 해보자 : predict
    y_pred = lr.predict(x) # 이 모델에 x를 집어넜었을 때 어떤 결과가 나올까

    # 예측값을 그려보자
    plt.plot(x, y_pred)
    plt.show()





