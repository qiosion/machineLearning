import pandas as pd
import random as r

# AI 엔지니어링 학과 22명 이름 모두 입력, 학번을 바르게 수정하는 코드를 작성

# 이름과 학번이 들어가는 딕셔너리 생성
dict = {"name" : [], "id" : []}

# 딕셔너리 -> 데이터프레임
df = pd.DataFrame(dict)

# 국어, 영어, 수학 과목 칼럼 추가
df["국어"] = 0
df["영어"] = 0
df["수학"] = 0
df["성별"] = []

# 이 과목들에 랜덤하게 넣어줄 점수 함수 생성
def score():
    return r.randint(0,100) # 랜덤한 정수타입 randint, 범위는 0~100

# 성별을 랜덤하게 넣는 함수 생성
def sex():
    return r.choice(['여','남'])

# 학번
for i in range(1, 23):
    df.loc[i] = ["name",
                 "2023-{0}".format(i),
                 score(), score(), score(), sex()]

# # 성별 : 하드코딩.. ㅎ
# df["성별"] = ['여자', '여자', '여자', '여자', '여자', '여자', '남자', '여자',
#              '남자', '여자', '남자', '남자', '남자', '여자', '남자', '남자',
#              '여자', '남자', '남자', '여자', '남자', '여자']
# 이름 : 하드코딩..
# df.loc[0, "name"] = ""
df.loc[1, "name"] = "강은선"
df.loc[2, "name"] = "구보람"
df.loc[3, "name"] = "김권아"
df.loc[4, "name"] = "김나은"
df.loc[5, "name"] = "김은희"
df.loc[6, "name"] = "김지아"
df.loc[7, "name"] = "김춘수"
df.loc[8, "name"] = "김해림"
df.loc[9, "name"] = "민필규"
df.loc[10, "name"] = "박민영"
df.loc[11, "name"] = "박용기"
df.loc[12, "name"] = "박제현"
df.loc[13, "name"] = "윤호원"
df.loc[14, "name"] = "이수경"
df.loc[15, "name"] = "이승우"
df.loc[16, "name"] = "이승현"
df.loc[17, "name"] = "장서화"
df.loc[18, "name"] = "전준범"
df.loc[19, "name"] = "정시영"
df.loc[20, "name"] = "정은비"
df.loc[21, "name"] = "최성민"
df.loc[22, "name"] = "황민설"

print(df)

# 데이터프레임을 파일로 저장하기
df.to_csv("ai_score_data.csv", index=None)