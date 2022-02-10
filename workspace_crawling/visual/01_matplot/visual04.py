import matplotlib.pyplot as plt
import random

# fig = plt.figure()
# ax01 = fig.add_subplot(2,2,1)
# ax02 = fig.add_subplot(2,2,2)
# ax03 = fig.add_subplot(2,2,3)
# ax04 = fig.add_subplot(2,2,4)

# 위에 껄 쉽게 만들기
fig, ax = plt.subplots(2,2,figsize=(10,10))

x = list(range(50))
y01 = list(random.randint(0, 50) for i in range(50))
y02 = list(random.randint(0, 50) for i in range(50))
y03 = list(random.randint(0, 50) for i in range(50))
y04 = list(random.randint(0, 50) for i in range(50))

# print(x)
# print(y01)
# print(y02)
# print(y03)
# print(y04)

# 산점도 (scatter) : 분포도
ax[0, 0].scatter(x, y01, color='r')
ax[0, 1].scatter(x, y02, color='g')
ax[1, 0].scatter(x, y03, color='b')
ax[1, 1].scatter(x, y04, color='y')

ax[0, 0].set_title('y01')
ax[0, 1].set_title('y02')
ax[1, 0].set_title('y03')
ax[1, 1].set_title('y04')

# 자동 레이아웃 조정
fig.tight_layout()

plt.show()


