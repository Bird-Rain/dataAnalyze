import pandas as pd # csv 읽기와 데이터 관리를 위한 라이브러리
import seaborn as sns # 히트맵 생성을 위한 라이브러리
import matplotlib.pyplot as plt # 데이터 시각화를 위한 라이브러라



data = pd.read_csv("Data.csv") # 데이터 파일 읽기
print(data.isnull().sum()) # 퍼블리셔와 출시연도에 결측치 발견. 둘 다 이번 분석에 활용 X -> 드롭처리
data = data.drop(["index", "Publisher", "Year"], axis=1) # 인덱스와 퍼블리셔 드롭처리 (인덱스와 랭크는 거의 동일한 데이터, 퍼블리셔는 이번 분석에 활용 X)
print(data.isnull().sum()) # 결측치 X

numeric_data = data.select_dtypes(include=["int64", "float64"]) # 숫자형태의 데이터만 선택
corr_data = numeric_data.corr() # 상관계수 계산
print(corr_data) # 계산된 연관도 확인

# 히트맵 파트
plt.figure(figsize=(12, 9)) # 창 크기 조절
sns.heatmap(corr_data) # 상관계수를 사용해 히트맵 생성
plt.title("corr HeatMap") # 한글 사용시 글자 깨짐.
plt.show() # 그래프 표시
 
 
# 인기 플랫폼 파트
print(data["Platform"].unique()) # 순위에 존재하는 플랫폼 확인
popular_Platform = data["Platform"].value_counts() # 전체 리스트에서 플랫폼별 사용횟수 카운트


