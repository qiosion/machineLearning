import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv("salmon_bass_data.csv")

    # 읽어들인 data Frame을 class 별로 나누겠다
    df_salmon = df.loc[df["Class"] == "Salmon"]
    df_bass = df.loc[df["Class"] == "Bass"]

    # print(df_salmon.info())

    # 히스토그램으로 표현
    # 이때 칸을 20개로 나눈다 : bins=
    # 보기좋게 투명도 0.5로 준다 : alpha=
    # 라벨도 붙인다 : label=""

    # 길이 Length
    plt.hist(df_salmon["Length"], bins=20, alpha=0.5, label="Salmon")
    plt.hist(df_bass["Length"], bins=20, alpha=0.5, label="Bass")
    plt.legend(loc="best") # 도표 구분하는걸 넣어줘. loc 위치는.. 니가 최선을 다해 골라봐라
    plt.title("Length Histogram") # 도표의 이름 붙여줌
    plt.show()

    # 밝기 Lightness
    plt.hist(df_salmon["Lightness"], bins=20, alpha=0.5, label="Salmon")
    plt.hist(df_bass["Lightness"], bins=20, alpha=0.5, label="Bass")
    plt.legend(loc="best") # 도표 구분하는걸 넣어줘. loc 위치는.. 니가 최선을 다해 골라봐라
    plt.title("Lightness Histogram") # 도표의 이름 붙여줌
    plt.show()

