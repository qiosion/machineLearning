import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
print(df_train['Survived'].value_counts())
# 0 = 사망 / 1 = 생존
    - 0 : 549
    - 1 : 342
"""
df_train = pd.read_csv('train.csv')
# print(df_train.corr())

# 생존 / 사망 그룹으로 Data Frame 나누자
survive = df_train.loc[df_train['Survived'] == 1].copy()  # 따로 사용하기위해 copy 함
dead = df_train.loc[df_train['Survived'] == 0].copy()

# 카테고리 별 생존자 히스토그램
def show_count_plot(feature):
    sns.countplot(data=df_train, x=feature, hue='Survived')  # hue : 카테고리
    plt.show()

# 생존자 중 해당 카테고리 비율
def show_survive_rate(feature):
    # feature 열에 대해, 생존자/사망자 count
    survive_count = survive[feature].value_counts(sort=False)
    print(survive_count)

    # survive_count.index 의 인덱스를 가지고 pie 플롯을 그리자
    category = survive_count.index

    plt.title("Survival Rate in {0}".format(feature))
    plt.pie(survive_count, labels=category, autopct='%.1f')

    # % 문자를 사용하고싶다면 두번 작성해준다
    # plt.pie(survive_count, labels=category, autopct='%.1f%%')
    plt.show()

# 카테고리 별 생존자 비율
def showSurvivedRate_Category(feature):
    survive_count = survive[feature].value_counts(sort=False)
    dead_count = dead[feature].value_counts(sort=False)

    length = len(survive_count.index)

    for i, index in enumerate(survive_count.index):
        plt.subplot(1, length, i+1)
        plt.pie([survive_count[index], dead_count[index]], labels=['Survived', 'Dead'], autopct="%.1f%%")
        plt.title(f"Survival rate of {index}")
    plt.show()

if __name__ == '__main__':

    # 좌석 등급에 따른 생존 여부를 histogram 으로 그려보자
    df_train['Survived'] = df_train['Survived'].replace(1, "Alive").replace(0, "Dead")
    df_train['Pclass'] = df_train['Pclass'].replace(1, "First")\
        .replace(2, "Business").replace(3, "Economy") # 역슬래시 + 엔터 치면 아직 줄이 덜끝난걸 알려줌

    sns.set_theme(style='darkgrid')

    # sns.countplot(data=df_train, x='Pclass', hue='Survived') # hue : 카테고리
    # plt.show()

    # 반복하게 되는 기능이므로 그냥 함수로 만들어서 쓴다
    show_count_plot("Pclass")
    show_count_plot("Age") # 나이에 따른 생존 여부

    show_survive_rate("Pclass")
    show_survive_rate("Sex") # 성별에 따른 생존 여부

    # 카테고리 별 생존자 비율 (모수 : 해당 카테고리 전체인원)
    showSurvivedRate_Category("Pclass")
    showSurvivedRate_Category("Sex")
