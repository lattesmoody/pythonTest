- 마지막 10개의 행 확인
df_score.tail(10)


[판다스 활용: 통계]

idxmax()/idxmin() 최댓값/최솟값을 갖는 인덱스 확인

cumsum() 누적 합 계산

std(): 표준편차

df.describe() 데이터의 통계정보 요약
* 수치형 데이터 아니면 다른 요약 통계 보여준다.



corr()/cov() 메서드

-------
데이터프레임과 시리즈는 형태가 다르게 나온다.

unique() : 시리즈에서 중복값 없앨 경우.

value_counts() 메서드: 값들의 빈도수 확인.

/* 데이터 특성이 겹치는 걸 뽑아내어 가공. 기존 두 개는 날려버리는게 정석.
iris_features_added = pd.concat([iris_features, length_property1], axis=1)

assert iris_features_added.shape == (150, 5)
iris_features_added
*/

- 정규화를 거치면 인공지능의 성능이 올라간다. (필수! 수치형 데이터에.)

- 표준화: 양쪽에 데이터를 분산? 시킨다.

- '열'을 인공지능에서는 '피처'라고 한다.


- boston["AGE_year"] = boston.AGE.astype(int) # 정수로 변경.

- boston.drop(["AGE"], axis=1, inplace=True) # axis = 1 반드시 명시해야 dorp 됨.

===============
[pandas_5 데이터 결합]

* 중요파트: - left_on과 right_on: 합병 기준으로 사용될 열을 따로따로 지정

..

### 인덱스 기준 합병

