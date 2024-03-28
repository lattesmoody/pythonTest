import numpy as np
import matplotlib.pyplot as plt
# [matplotlib.pyplot 1부]

# plt는 pyplot의 줄임말.

# * ctrl + space는 해당 파라미터에 들어갈 것을 추천
# * ctrl + shift + space는  IntelliSense 추천 기능을 활성화

# * 시각화는 분석 후 보여주기 때문에 통찰을 얻을 수 있다. (굉장히 중요. (30% 이상))


# [plot() 함수]

# [마커]

"""
ypoints = np.array([5, 1, 2, 10, 7, 9])

plt.plot(ypoints, marker='*')
plt.show()
"""

"""
ypoints = np.array([5, 1, 2, 10, 7, 9])

plt.plot(ypoints, 'o:g')
plt.show()
"""

"""
y1 = np.array([5, 1, 2, 10, 7, 9])
y2 = np.array([3, 7, 4, 2, 9, 6])

plt.plot(y1)
plt.plot(y2)

plt.show()
"""


# 라벨과 제목 <- 간과하는 경우가 있음, 
# 그러나 다른 사람이 본다고 생각하고 잘 작성해두기(알아보기 쉽게)

"""
x = np.array([25, 80, 85, 35, 48, 90, 95, 77, 88, 56, 15, 20, 33, 69, 44])
y = np.array([35, 90, 70, 40, 55, 95, 90, 80, 90, 65, 25, 25, 44, 77, 45])

plt.xlabel("Python score")
plt.ylabel("Machine Learning Score")

plt.plot(x, y, 'o')

plt.show()
"""

# 범위 지정: plt.axis([x축의 최솟값, x 축의 최댓값, y축의 최솟값, y축의 최댓값])

# 척도 지정: plt.gca().set_aspect("equal")

# 색지도: 색 리스트 
# 예) magma, viridis, gray(흑백 색지도)


"""
data = np.random.rand(10, 10)

# 히트맵 그리기
plt.imshow(data, cmap='viridis')
plt.colorbar()  # 컬러바 추가
plt.show()
"""




