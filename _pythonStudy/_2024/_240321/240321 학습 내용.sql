<판다스 데이터프레임]>
[시리즈]
: 1차원 어레이 (직렬화)

   - 리스트와 어레이 활용
   - 사전 활용
   -  중복 인덱스 허용
   -  in 연산자
   -  결측치 사용 여부 확인 pd.isnull() / pd.notnull()
   -  isnull().any(): True이면 결측치가 있다.
   -  notnull().all() : False 이면 결측치가 있다.

[데이터 프레임]
: 인덱스를 공유하는 여러 개의 시리즈를 다루는 객체다.
-  데이터프레임 생성
   -  pd.concat() 함수 활용. 
      -  (axis = 0은 밑으로 붙이고, axis=1은 옆으로 붙인다.)
  

   - 리스트 사전 활용
   - 중첩 사전 활용 (구조 잘 확인 하기 - json도 같은 구조를 띄고 있다.)


- `name` 과 `values`

   - name 속성 => qhxhd 행 이름, 열 이름 지정할 때 사용.
   - values 속성

-  `columns` 와 `index`
   - columns 속성
   예)
   frame2_ = frame2.copy()
   frame2_["debt2"] = np.linspace(0, 1, 9)   # 구간 [0, 1]을 8개의 구간으로 쪼개기

   frame2_


   - index 속성 

   * index와 column을 동시에 지정 가능.

   - 중복 인덱스 허용
   

   - index 객체
  

[데이터프레임 연산]

   - in 연산자

   (데이터 일부분만 확인하려 할 때)
   - head() 메서드: 앞부분 볼 수 있음.     
   - tail() 메서드: 마지막의 데이터 확인. 

   - 전치 데이터 프레임 예) frame3.T 또는 frame3.transpose()
   - 결측치 사용 여부 확인. => isnull(), notnull()
   - any(),  all() - axis 지정 가능

   - np.any(), np.all()



* 시각화에는 여러 종류가 있음
1. pandas
2. matplotlib
3. seaborn
4. plotly
