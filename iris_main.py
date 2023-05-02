import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 나의 분류기
# 입력 : 4종 : sepal length, sepal width, petal length, petal width
# 출력 : 3종 : setosa, versicolor, virginica
def my_clf(x):
    # petal length 가 2.45보다 작으면 세토사
    if x[2] < 2.45:
        return "Iris-setosa"
    else:
        if x[3] <= 1.7 and x[2] <= 5.1:
            return "Iris-versicolor"
        else:
            return "Iris-virginica"


if __name__ == "__main__":
    df = pd.read_csv("Iris.csv")
    # print(df.head()) # 디폴트로 최초 5개 보여줌
    df = df.drop(["Id"], axis=1) # Id열을 세로(종방향, 1번축 방향)으로 날림
    # print(df.info())

    # print(df["Species"].value_counts()) # 안에 각 클래스별로 데이터가 몇개가 있는지 세어줌

    # print(my_clf([6.5, 2.8, 4.6, 1.5])) # Iris-versicolor

# 모델의 정확도를 확인해보자
    # 대상의 feat 부분과 정답 부분을 나눈다
    X = df.iloc[:, :4] # row은 전부 다, col은 4개[0,1,2,3 -> 4번인덱스인 종 species은 떨어져나감]
    y = df.iloc[:, -1] # row는 전부 다, col은 맨 뒤 한개만
    # print(X)
    # print(y)

    # X에서 자료 하나 빼서 확인해보면
    # print(my_clf(X.iloc[0])) # Iris-setosa

######### 앙상블의 Random Forest 사용 #########
    # 3개의 인자를 초기화
    clf = RandomForestClassifier(n_estimators=10,
                                 max_depth=3,
                                 random_state=0)

    clf.fit(X, y)
    print(clf.score(X, y)) # 0.9733333333333334
    # score : 만들어진 모델에 X, y를 주면
    # 내부적으로 X를 넣었을 때 튀어나온 값과 y를 비교하여 계산해줌

    # 계산. 2차원 배열로 만들어서 해줘야함
    print(clf.predict([[4.7, 3.2, 1.3, 0.2]])) # Iris-setosa

######### 이하 직접 구현한 것 #########
    # hit = 0
    # miss = 0
    #
    # for i in range(150):
    #     if my_clf(X.iloc[i]) == y[i]:
    #         hit += 1
    #     else:
    #         miss +=1
    # print("hit : ", hit)
    # print("miss : ", miss)
    # print(hit / (hit + miss) * 100)

######### 직접 구현한 후로는 여기 밑으론 없어도 됨 #########

# 각 칼럼 간의 상관관계 시각화
    # 종에 따라서 각 칼럼들 간의 상관관계를 그래프로 뽑는다
    # sns.pairplot(df, hue="Species")
    # plt.show()

# 구현해보자
    # 데이터 프레임을 나누어 봄
    # df_setosa = df[df["Species"] == "Iris-setosa"] # 파란색. 젤 밑값
    # df_versicolor = df[df["Species"] == "Iris-versicolor"] # 주황색
    # df_virginica = df[df["Species"] == "Iris-virginica"] # 초록색. 젤 큰값
    # 맞게 나눴는지 확인     # print(df_setosa)

    # setosa와 versicolor를 구분하기 위해
    # df_setosa의 최대값과 df_versicolor의 최소값을 찾아보자
    # print(df_setosa["PetalLengthCm"].max()) # 1.9
    # print(df_versicolor["PetalLengthCm"].min()) # 3.0
    # 1.9와 3.0의 중간값인 2.45를 선택 !

    # # scatter 구현
    # # 단, versicolor와 virginica 만 그려보자
    # plt.figure(figsize=(14, 12))
    # # 벌시칼라
    # plt.scatter(df_versicolor["PetalLengthCm"], # Y축
    #             df_versicolor["PetalWidthCm"]) # X축
    # # 버지니카
    # plt.scatter(df_virginica["PetalLengthCm"], # Y축
    #             df_virginica["PetalWidthCm"]) # X축
    #
    # # x축 범위 보기 힘드니까 좀 늘림. 3.0에서 7.0까지 0.1간격으로
    # plt.xticks(np.arange(3.0, 7.0, 0.1))
    # # y축에도 눈금 만들어
    # plt.yticks(np.arange(1.0, 2.6, 0.1))
    # # 구분 편하게 격자도 만들어
    # plt.grid(True)
    #
    # # 헷갈리니까 라벨 달아주자
    # plt.xlabel("Length")
    # plt.ylabel("Width")
    # # plt.show()



