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


# 인기 장르 파트 (플랫폼 파트 수정하여 사용)
print(data["Genre"].unique()) # 데이터에 존재하는 장르 종류 확인
popular_Genre = data["Genre"].value_counts() # 전체 리스트에서 장르별 게임 수 카운트
plt.figure(figsize=(12, 6)) # 창 크기 조절
plt.bar(popular_Genre.index, popular_Genre.values, color='skyblue') # 막대 그래프 생성 x-> 장르 이름 y-> 해당 장르의 게임이 순위에 등록된 수
plt.title("Number of Games per Genre", fontsize=16) # 타이틀 (한글 깨짐)
plt.xlabel("Genre", fontsize=14) # x 레이블 설정
plt.ylabel("Count", fontsize=14) # y 레이블 설정
plt.grid(axis='y', linestyle='--', alpha=0.7) # 가로줄 추가
plt.show() # 그래프 표시



