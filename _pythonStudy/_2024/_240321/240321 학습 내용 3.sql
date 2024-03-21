<판다스 10분 완성 1부>

[시리즈와 데이터프레임]

- 데이터프레임 객체 생성
    방식1)

    dates = pd.date_range(start="20130101", periods=6)
    ..
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    방식2) 사전 객체 이용 ??

[데이터 살펴보기]

- 데이터프레임을 to_numpy() 를 적용

- 수치형 데이터의 분포 확인
df.describe()

- 전치 데이터프레임
df.T

- 열 라벨 내림차순 정렬
df.sort_index(axis = 1, ascending=False) 

- 특정 열의 값을 기준으로 행 정렬
df.sort_values(by='B')

[인덱싱/슬라이싱]
- 열 인덱싱
- 행 슬라이싱

[라벨 인덱싱/슬라이싱 loc[]]

[위치 인덱싱/슬라이싱 iloc[]]

[리인덱싱]

[부울 인덱싱]
    * isin() 메서드

[항목 지정]

[where()/mask() 메서드 활용]

...
(중간부분 확인 필요.)
...
다음 시간은 [이산화]