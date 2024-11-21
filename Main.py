import pandas as pd # csv 읽기와 데이터 관리를 위한 라이브러리
import seaborn as sns # 히트맵 생성을 위한 라이브러리
import matplotlib.pyplot as plt # 데이터 시각화를 위한 라이브러라


# 전처리
data = pd.read_csv("Data.csv") # 데이터 파일 읽기
print(data.isnull().sum()) # 퍼블리셔와 출시연도에 결측치 발견. 둘 다 이번 분석에 활용 X -> 드롭처리
data = data.drop(["index", "Publisher", "Year", "Game Title"], axis=1) # 인덱스와 퍼블리셔 드롭처리 (인덱스와 랭크는 거의 동일한 데이터, 게임 타이틀, 퍼블리셔는 이번 분석에 활용 X)
print(data.isnull().sum()) # 결측치 X


# 히트맵 파트
numeric_data = data.select_dtypes(include=["int64", "float64"]) # 숫자형태의 데이터만 선택
corr_data = numeric_data.corr() # 상관계수 계산
print(corr_data) # 계산된 연관도 확인
plt.figure(figsize=(12, 9)) # 창 크기 조절
sns.heatmap(corr_data) # 상관계수를 사용해 히트맵 생성
plt.title("corr HeatMap") # 한글 사용시 글자 깨짐.
plt.show() # 그래프 표시
 
 
# 인기 플랫폼 파트
print(data["Platform"].unique()) # 데이터에 존재하는 플랫폼 종류 확인
popular_Platform = data["Platform"].value_counts() # 전체 리스트에서 플랫폼별 사용횟수 카운트
plt.figure(figsize=(12, 6)) # 창 크기 조절
plt.bar(popular_Platform.index, popular_Platform.values, color='skyblue') # 막대 그래프 생성
plt.title("Number of Games per Platform", fontsize=16) # 타이틀 (한글 깨짐)
plt.xlabel("Platform", fontsize=14) # x 레이블
plt.ylabel("Count", fontsize=14) # y 레이블 
plt.grid(axis='y', linestyle='--', alpha=0.7) # 가로줄 추가
plt.show() # 그래프 표시

# 수익성 높은 플랫폼


# 인기 장르 파트 (플랫폼 파트 수정하여 사용)
print(data["Genre"].unique()) # 순위에 존재하는 플랫폼 확인
popular_Genre = data["Genre"].value_counts() # 전체 리스트에서 플랫폼별 사용횟수 카운트
plt.figure(figsize=(12, 6)) # 창 크기 조절
plt.bar(popular_Genre.index, popular_Genre.values, color='skyblue') # 막대 그래프 생성
plt.title("Number of Games per Genre", fontsize=16) # 타이틀 (한글 깨짐)
plt.xlabel("Genre", fontsize=14) # x 레이블
plt.ylabel("Count", fontsize=14) # y 레이블 
plt.grid(axis='y', linestyle='--', alpha=0.7) # 가로줄 추가
plt.show() # 그래프 표시

# 수익성 높은 장르



