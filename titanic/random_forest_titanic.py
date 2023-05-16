import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

df_train = pd.read_csv('train.csv')
# print(df_train.info())

###################################### 전처리 ######################################
# 관련 없을 것이라 생각되는 열 삭제
df_train = df_train.drop(["Name", "PassengerId", "Ticket", "Fare", "Cabin"], axis=1)
# print(df_train.info())

# 비어있는 데이터 NaN 채우기
print(df_train.isnull().sum()) # 빈 데이터 수

# age는 평균으로 채우자
df_train["Age"] = df_train["Age"].fillna(df_train["Age"].mean())

# 탑승 항구는 null값이 2개밖에 없으니, 버리든지 제일 많은 값(S)로 채운다
df_train["Embarked"] = df_train["Embarked"].fillna("S")

# 문자로 되어있는 데이터를 숫자로 바꿈
# 성별 Sex -> map을 통해 {male: 0, female: 1}
df_train["Sex"] = df_train["Sex"].map({"male": 0, "female": 1})

# 항구 Embarked -> Q: 0, C: 1, S: 2
df_train["Embarked"] = df_train["Embarked"].map({"Q": 0, "C": 1, "S": 2})

###################################### 학습할 모델 만들기 ######################################
# 모델 가지고 옴
clf = RandomForestClassifier()
# clf = DecisionTreeClassifier()
# clf = SVC()

# 특징과 정답을 X, Y로 분리
y = df_train["Survived"]
x = df_train.drop("Survived", axis=1)

# 학습 -> 시간 많이걸리는 작업이니까 다른거 할때는 일단 막아두자
clf.fit(x, y)
print(clf.score(x, y))

###################################### 테스트 데이터 셋 예측 ######################################
# test 데이터 가져오기
df_test = pd.read_csv('test.csv')

# 예측할 때, 입력값은 학습을 했을 때 모양과 같아야 함
# id는 나중에 답지를 낼 때 써야하니까, 따로 빼놓는다
pId = df_test["PassengerId"]
# 학습할 때 삭제했던 열을 똑같이 삭제하자
df_test = df_test.drop(["Name", "PassengerId", "Ticket", "Fare", "Cabin"], axis=1)

# 비어있는 값을 채워준다
df_test["Age"] = df_test["Age"].fillna(df_test["Age"].mean())

# 문자로 되어있는 데이터를 숫자로 바꿈
# 성별 Sex -> map을 통해 {male: 0, female: 1}
df_test["Sex"] = df_test["Sex"].map({"male": 0, "female": 1})

# 항구 Embarked -> Q: 0, C: 1, S: 2
df_test["Embarked"] = df_test["Embarked"].map({"Q": 0, "C": 1, "S": 2})

###################################### 분류기 확인 ######################################
# 분류기에 테스트 데이터를 넣어준다
result = clf.predict(df_test)
print(result)

# 제출파일을 만들자
submit = pd.DataFrame({"PassengerId": pId, "Survived": result})
submit.to_csv("test1.csv", index=False)