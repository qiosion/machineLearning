import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree

if __name__ == "__main__":
    df = pd.read_csv("salmon_bass_data.csv")

    # # 첫번째 물고기의 데이터
    # X = [[2, 0.8]]
    # Y = [["Salmon"]]

    X = []
    Y = []

    for i in range(len(df)): # len(df) = 318
        # fish는 두개가 엮여서 배열이 됨
        fish = [df.loc[i, "Length"],  # 데이터 중 i번째의 "Length" 값을 가져와라
                df.loc[i, "Lightness"]] # [i, "Lightness"]의 값을 가져와라
        X.append(fish) # => X값
        Y.append(df.loc[i, "Class"]) # => Y값. Salmon / Bass

    # Decision Tree 디시전 트리를 생성하여 학습한다
    dtree = tree.DecisionTreeClassifier()
    dtree = dtree.fit(X, Y) # 학습

    # 그림 그려보자. tree.plot_tree(dtree)를 제외한 나머지는 그냥 옵션일 뿐임
    plt.figure(figsize=(10, 10))
    tree.plot_tree(dtree, fontsize=8, filled=True,
                   class_names=["Salmon", "Bass"],
                   feature_names=["Length", "Lightness"])
    # plt.show()

    # 예측하기 predict
    result = dtree.predict([[5, 5.5]])
    print(result)
