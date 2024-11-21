import pandas as pd # csv 읽기와 데이터 관리를 위한 라이브러리
import seaborn as sns # 히트맵 생성을 위한 라이브러리
import matplotlib.pyplot as plt # 데이터 시각화를 위한 라이브러라


print("Hello")


data = pd.read_csv("Data.csv") # 데이터 파일 읽기

numeric_data = data.select_dtypes(include=["int64", "float64"]) # 숫자형태의 데이터만 선택
corr_data = numeric_data.corr() # 상관계수 계산

print(data["Platform"].unique()) # 순위에 존재하는 플랫폼 확인
popular_Platform = data["Platform"].value_counts() # 전체 리스트에서 플랫폼별 사용횟수 카운트


