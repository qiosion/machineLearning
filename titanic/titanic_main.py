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
def showSurvivedRate_Category(feature): # 간단버전
    survive_count = survive[feature].value_counts(sort=False)
    dead_count = dead[feature].value_counts(sort=False)

    length = len(survive_count.index)

    for i, index in enumerate(survive_count.index):
        plt.subplot(1, length, i+1)
        plt.pie([survive_count[index], dead_count[index]], labels=['Survived', 'Dead'], autopct="%.1f%%")
        plt.title(f"Survival rate of {index}")
    plt.show()

def show_group_rate(feature): # 수업버전
    sur_info = survive[feature].value_counts(sort=False)
    dead_info = dead[feature].value_counts(sort=False)

    # print(sur_info)  # female 233, male 109
    # print(dead_info)  # female 81, male 468

    # print(sur_info["male"])  # 109
    # print(dead_info["male"])  # 468

    print(sur_info.index)  #
    print(dead_info.index)  #

    # 서브플롯
    fig = plt.figure(figsize=(14, 8))
    plt.title("survival rate of " + feature)

    for i, index in enumerate(sur_info.index):
        # subplot 을 인덱스 길이만큼, i+1번째 것을 그린다 (i는 0부터 시작하므로 +1해줌)
        fig.add_subplot(1, len(sur_info.index), i+1)
        plt.pie([sur_info[index], dead_info[index]],
                labels=["Alive", "Dead"],
                autopct="%0.1f%%")
        plt.title("Survival rate of " + str(index))
    plt.show()

    """
    # feature 안의 index 로 자동화 하는것
    print("생존자의 인덱스 별 생존자 수 확인")
    for index in sur_info.index:
        print(index) # female # male
        print(sur_info[index]) # 233 # 109
        print(dead_info[index]) # 31 # 468
    """

if __name__ == '__main__':

    df_train['Survived'] = df_train['Survived'].replace(1, "Alive").replace(0, "Dead")

    sns.set_theme(style='darkgrid')

    """
    # 좌석 등급에 따른 생존 여부를 histogram 으로 그려보자
    df_train['Pclass'] = df_train['Pclass'].replace(1, "First")\
        .replace(2, "Business").replace(3, "Economy") # 역슬래시 + 엔터 치면 아직 줄이 덜끝난걸 알려줌

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
    
    # 카테고리별 생존자 - 수업버전
    
    print("좌석 등급 별 생존자 수")
    sur_info_Pc = survive["Pclass"].value_counts()
    print(sur_info_Pc) # 136, 119, 87
    
    show_group_rate("SibSp")
    show_group_rate("Sex")
    """

    # 나이를 그룹별로 나누어 처리
    # 비어있는 값을 평균값으로 채워보자
    df_train["Age"].fillna(df_train["Age"].mean(), inplace=True)
    print(df_train.info())

    # 나이를 연령대 별로 나눌 것이다
    for i in range(len(df_train)): # 전체 데이터를 확인
        age = int(df_train.loc[i, "Age"] / 10) # i행의 Age 열에 있는 값을 10으로 나눠서 정수만 취한다
        if age > 7:
            age = 7
        df_train.loc[i, "Age"] = age

    # 생존 / 사망 그룹에 다시 df_train을 넣어준다
    survive = df_train.loc[df_train['Survived'] == "Alive"].copy()  # 따로 사용하기위해 copy 함
    dead = df_train.loc[df_train['Survived'] == "Dead"].copy()

    show_group_rate("Age")





