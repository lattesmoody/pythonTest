[데이터프레임 인덱싱]

- 리인덱싱

- 시리즈 리인덱싱
    * 새로운 인덱스 추가 (NaN이 생긴다.)
    * 리인덱싱 과정 시 mapping 할 때 인덱스를 지정하지 않은 것은 제외된다.
    * reindex() 메서드는 기본적으로 행의 index에 대해 작동한다.
    예) 새로운 b 인덱스가 들어오면 해당 b 행의 값들은 모두 NaN. 

    - 리인덱싱과 결측치
    * 결측치 채우기 1: method 키워드 인자
    => `method='fill'` 키워드 인자는 결측치를 위쪽에 위치한 값으로 채운다.

        __주의사항:__ 인덱스가 오름 또는 내림 차순으로 정렬되어 있는 경우에만
        참고1 * method = 'ffill'  * 위쪽에 위치한 값이 없으면 결측치가 된다.
        참고2 * method = 'bfill'의 경우 아랫쪽에 있는 값으로 채울 수도 있다.
        참고3 * method = 'nearest'의 경우 가장 가까운 곳에 있는 값

    * 결측치 채우기 2: fill_value 키워드 인자
        * 결측치 발생 시 해당 결측값을 지정값으로 대체 가능하다. 


- 시리즈 인덱싱/슬라이싱
    * 시리즈 인덱싱

    * 시리즈 슬라이싱
    주의사항: 정수가 아닌 다른 인덱스 라벨을 이용하는 슬라이싱은 
    양쪽 구간의 끝을 모두 포함하는 점이 다르다.

    * 시리즈 팬시 인덱싱 (인덱스 라벨 활용 / 정수 인덱스 활용)

- 데이터 프레임 인덱싱
    * 열 인덱싱
    * 열 팬시 인덱싱
    * 열 업데이트
      예1) df['debt'] = 16.5
      예2) df['debt'] = np.arange(9.)
    * 부울 인덱싱(필터링)

    * 행 인덱싱 (행의 값을 추출..)
        ** loc() 함수 예)  data.loc['Colorado']
        ** iloc() 함수 예) data.iloc[2] 

[데이터프레임 슬라이싱: `loc()`과 `iloc()` 함수]
    * 열 슬라이싱
        ** 예1) data.iloc[2:, :]
        ** 예2) data.iloc[2]

    * 스텝 활용

    * 인덱싱과 슬라이싱 조합.

    * 부울 인덱싱(필터링) 연속 적용


