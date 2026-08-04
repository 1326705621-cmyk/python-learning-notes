# ---------- 1. 读取输入版 ----------
n = int(input())  # 先读取第一行，得到挡板个数

# 读取第二行所有数字（比如 "3 1 4"），按空格拆开
input_str = input()          # 得到 "3 1 4"
str_list = input_str.split() # 得到 ["3", "1", "4"]

h = []  # 用来存放真正的数字高度
for s in str_list:
    h.append(int(s))         # 把 "3" 变成 3，放进 h

# 如果只有1块挡板，没水可存，直接结束
if n <= 1:
    print(0)
    exit()

# ---------- 2. 计算左侧最高挡板 ----------
# 先造一个长度为 n 的“架子”，里面全是 0
left_max = []
for i in range(n):
    left_max.append(0)       # 这样 left_max 就是 [0, 0, 0, ...]

# 第 1 块挡板（下标0）的左边最高就是它自己
left_max[0] = h[0]

# 从第 2 块挡板开始往右算
i = 1
while i < n:
    # 当前左侧最高 = max(上一个左侧最高, 当前挡板高度)
    if left_max[i-1] > h[i]:
        left_max[i] = left_max[i-1]
    else:
        left_max[i] = h[i]
    i = i + 1

# ---------- 3. 计算右侧最高挡板 ----------
right_max = []
for i in range(n):
    right_max.append(0)      # 同样造一个全是 0 的架子

# 最后 1 块挡板（下标 n-1）的右边最高就是它自己
right_max[n-1] = h[n-1]

# 从倒数第 2 块挡板开始往左算
i = n - 2
while i >= 0:
    # 当前右侧最高 = max(上一个右侧最高, 当前挡板高度)
    if right_max[i+1] > h[i]:
        right_max[i] = right_max[i+1]
    else:
        right_max[i] = h[i]
    i = i - 1

# ---------- 4. 计算总存水量 ----------
total_water = 0

# 遍历每个槽位（挡板 i 和 i+1 之间）
i = 0
while i < n - 1:
    left_height = left_max[i]      # 槽位左边最高
    right_height = right_max[i+1]  # 槽位右边最高
    
    # 水面高度 = 左右最高中较矮的那个
    if left_height < right_height:
        water = left_height
    else:
        water = right_height
    
    total_water = total_water + water
    i = i + 1

# 输出最终答案
print(total_water)
