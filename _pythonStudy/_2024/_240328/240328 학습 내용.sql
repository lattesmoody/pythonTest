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