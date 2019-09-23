N, K = map(int, input().split())
S = input()

l = []
now = 1 # 今見ている数(1から見る配列を作りたいので1で初期化)
cnt = 0

# lには(1の個数),(0の個数),(1の個数),(0の個数),...(1の個数)という感じのリストを入れたい(両端が0から始まるとしても1が0こあるとしてカウントしたい)
for i in range(N):
    if int(S[i]) == now:
        cnt += 1
    else:
        l.append(cnt)
        cnt = 1
        now = 1 - now # 0と1を切り替える(now ^= 1でも良い)

if cnt != 0:
    l.append(cnt)
if len(l) % 2 == 0: # (1の個数),(0の個数),(1の個数),(0の個数),...(0の個数)となってしまっていたら最後に0を入れておく
    l.append(0)

ans = 0
width = 2 * K + 1

# 累積和
# 元のリストが[0, 1, 2, 3, 4, 5]の時に[0, 1, 2, 3, 4, 5, 6]のように個数は+1になる(つまり最初は0)
lsum = [0 for _ in range(len(l) + 1)] # len(l)+1個の要素
for i in range(len(l)): # 0からlen(l)まで
    lsum[i + 1] = lsum[i] + l[i]
# print(lsum)

for i in range(0, len(l), 2): # ここを2ごとにすることで1の個数を数えられる
    left = i
    right = min(i + width, len(l))
    tmp = lsum[right] - lsum[left] # [left, right)
    # print(left, right, tmp)
    ans = max(ans, tmp)

"""
# しゃくとり法

# ①forループの外側にleft,rightを持っておく
left = 0
right = 0
tmp = 0 # [left, right)の総和

for i in range(0, len(l), 2):
    # ②次のleft,rightを計算する
    nextleft = i # 0,2,4,...
    nextright = min(i + width, len(l)) # 0+width,2+width,...

    # ③左端の移動
    while nextleft > left:
        tmp -= l[left]
        left += 1

    # ③右端の移動
    while nextright > right:
        tmp += l[right]
        right += 1

    ans = max(ans, tmp)
"""

"""
# 愚直に足し算を繰り返すとTLE

for i in range(0, len(l), 2): # ここを2ごとにすることで1の個数を数えられる
    tmp = 0
    left = i
    right = min(i + width, len(l))
    for j in range(left, right): # leftからright-1まで
        tmp += l[j]
    ans = max(ans, tmp)
"""

print(ans)
