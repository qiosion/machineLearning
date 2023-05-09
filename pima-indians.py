import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv('pima-indians-diabetes3.csv')
    print(df)

    # 칼럼 pregnant,plasma,pressure,thickness,insulin,bmi,pedigree,age,diabetes
    # 당뇨 여부로 나눈다 diabetes
    sns.pairplot(df)
    plt.show()

