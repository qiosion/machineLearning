import pandas as pd
import random as r

def score():
    return r.randint(0,100) # 0부터 100 사이의 랜덤한 형태의 정수

# 함수 예제
def add(a, b):
    c = a + b
    return c

print(add(3, 4))

# 리턴값이 없는 함수
def add2(a, b):
    print("{0} {1} {0}".format(a, b)) # 포맷팅에 들어가는 수가 적어도 같은 {0}을 사용해서 나오긴 함
    print("{0} + {1} = {2} 입니다.".format(a, b, a+b))
c = add2(2, 3) # 리턴 값이 없음
print(c) # None

if __name__ == "__main__":
    print("Hello, World!")
    # 데이터 프레임 변수 df를 만들어서 csv를 읽어오겠다
    # df = pd.read_csv("salmon_bass_data.csv")
    # print(df)
    dict = {"name": ["강현우", "강은선"]}
    print(type(dict))

    # value 밸류 값에 리스트 넣을 수 있음
    nameList = ["강현우", "강은선", "구보람"]
    dict["name"] = nameList

    # 키 값을 인덱스처럼 쓰는게 가능
    print(dict["name"])

    # 다른 칼럼을 추가하고 싶다면? 추가하고 싶은 칼럼 명과 그 값을 주면 됨
    dict["id"] = ["2023-0", "2023-1"] # 2개만 주면 2개 주는대로 그냥 들어감
    print(dict)
    # value가 리스트이므로, list에서 쓰는 것들다 쓸 수 있음
    dict["id"].append("2023-2")
    print(dict)

    df = pd.DataFrame(dict)
    print(df)

    # 데이터프레임에 칼럼 추가
    # 하나의 값으로 열을 초기화
    df["국어"] = 0
    # 실제 값을 할당
    df["영어"] = [100, 95, 90]
    print(df)

    # 행에 접근할 때는 loc[index] 사용
    # 기존의 행 변경
    df.loc[0] = ["신주석", "2023-0", score(), score()]
    # 행 추가
    df.loc[3] = ["김권아", "2023-3", score(), score()]
    df.loc[4] = 0
    df.loc[df.shape[0]] = ["김은희", "2023-5", score(), score()]
    print(df)

    # loc[행, 열] 로 접근
    df.loc[1, "id"] # 데이터프레임은 1행의 id를 찾을때 자바처럼 [1]["id"] 적으면 에러남
    df.loc[1, "국어"] = score()
    df.loc[2, "국어"] = score()
    df.loc[4] = ["김나은", "2023-4", score(), score()]
    df["수학"] = [score(), score(), score(), score(), score(), score()]
    print(df)

    # 한번에 여러 데이터 추가
    for i in range(len(df), 23): # len(df)는 6. 즉 6~22까지 한번에 추가하려고 함
        df.loc[i] = ["name{0}".format(i), # 이름에 i를 넣음
                     "2023-{0}".format(i), # 학번
                     score(), score(), score()]
    print(df)

    df.to_csv("결과물 파일.csv")