import pandas as pd

df = pd.read_csv("ai_score_data.csv")

print(">>> 데이터 정보")
print(df.shape) # 전체 행과 열의 개수
print(df.info()) # 칼럼의 정보와 데이터타입

print(df.describe()) # 통계정보

print(">>> 통계정보의 개별접근")
# 특정 열의 평균
print("수학 평균 : ", df['수학'].mean())
print("수학 평균 : ", df.수학.mean())

# 중간값 (!=평균)
print("국어 중간값 : ", df['국어'].median())
print("국어 중간값 : ", df.국어.median())

# 최대/최소값
print("영어 최대값 : ", df.영어.max())
print("영어 최소값 : ", df.영어.min())

# 표준편차
print("수학의 표준편차 : ", df.수학.std())

# 두 열 사이의 상관계수 * 대괄호 [] 가 두개임!
# ,'\n' 는 왜해주는거야? 굳이 엔터 안해도 알아서 되는거같은데..
print(df[['수학', '국어']].corr(),'\n')
print(df[['수학', '영어']].corr(),'\n')
print(df[['국어', '영어']].corr(),'\n')

# 모든 열 사이의 상관계수
# print(df.corr()) # 이거. . 열에 이름이 있으니까 안되는거같음

# matplot 라이브러리 import
import matplotlib.pyplot as plt

# print(">>> 히스토그램")
# plt.hist(df['수학'])
# plt.show()
#
# plt.title('Math Score') # 제목
# plt.xlabel('Score') # x축 라벨
# plt.xticks(range(0, df["수학"].max(), 5)) # x축 범위(step)
# plt.ylabel('Count') # y축 라벨
# plt.hist(df['수학'], bins=20) # 히스토그램 구간(덩어리) 개수
# plt.show()

print(">>> 산점도(스캐터플롯)")
plt.scatter(df['수학'],df['영어'])
plt.show()

# plt.grid() # 격자표현
#
# # color, marker 모양
# plt.scatter(df['수학'], df['영어'], color='red', marker='P') # 플러스모양
#
# # 점 하나씩도 설정 가능
# plt.scatter(df.loc[0, '수학'], df.loc[0, '영어'], color='red', marker='s') # 사각형
# plt.scatter(df.loc[1, '수학'], df.loc[1, '영어'], color='blue', marker='D') # 다이아몬드
# plt.scatter(df.loc[2, '수학'], df.loc[2, '영어'], color='yellow', marker='h') # 헥사곤
# plt.scatter(df.loc[3, '수학'], df.loc[3, '영어'], color='green', marker='x') # x
#
# plt.show()

print(">>> 범주에 따른 산점도 표현")
canvas = plt.figure(figsize=(7.0, 7.0)) # 이미지 크기 조절

plt.xlabel("Math Score")
plt.ylabel("English Score")

for i in range(len(df['성별'])):
    if df.loc[i, '성별'] == '남자':
        plt.scatter(df.loc[i, '수학'], df.loc[i, '영어'], color='blue')
    else:
        plt.scatter(df.loc[i, '수학'], df.loc[i, '영어'], color='red')
plt.show()