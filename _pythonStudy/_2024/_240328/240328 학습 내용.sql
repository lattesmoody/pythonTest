[데이터 그룹화]

[데이터 집계]
* 중요 집계 매서드
1. first,last
2. nth
3. ohlc

* agg() 메서드: 사용자 정의 집계 함수를 그룹화 집계 함수로 사용.
예) grouped[["data1", "data2"]].agg(peak_to_peak)

* grouped_pct.agg("mean")
=> 여기서 "mean"은 문자열 "mean"이 아니라, 
평균값을 구하는 mean 메서드를 의미한다.


[apply: 다목적 데이터 집계]

tips.groupby("smoker").apply(top)
####################################

그룹화 적용
tips.groupby(["smoker", "day"]).apply(top, n=1, column="total_bill")
그룹화 제거
tips.groupby("smoker", group_keys=False).apply(top)


pd.cut 관련 내용은 나중에 복습.

#####################################
[예제: 무작위 샘플링]



[피벗 테이블]

tips.pivot_table(index=["time", "size", "smoker"], columns="day",
                 values="tip_pct", fill_value=0)

여기서 fill_value의 경우 nan 값을 0으로 모두 채워라.

################################
[Cross-Tabulations: Crosstab]
data = pd.read_table(StringIO(data), sep="\s+")

sep의 경우.. 스페이스바를 기준으로 나누어 읽어들임 (공백의 크기는 상관없음)