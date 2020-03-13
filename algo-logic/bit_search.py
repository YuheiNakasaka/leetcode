l = [4, 10, 1]

# 再帰版
def rec_plus(l, now, sum):
    if now < 3:
        return rec_plus(l, now + 1, sum + l[now]) + rec_plus(l, now + 1, sum)
    else:
        return sum

print(rec_plus(l, 0, 0))

# bitを各リストの値を選ぶか選ばないかのフラグとみると、
# 000,100,110,111,101,011,001,010の8通り。
# maskで100,010,001の３つを作り(1 << i)、
# bitとの論理積を取ればlistからその値を選ぶか選ばないかを求められる
def bit_plus(l):
    sum = 0
    for bit in range(1 << len(l)):
        for i in range(len(l)):
            mask = 1 << i
            if bit & mask:
                sum += l[i]
    return sum

print(bit_plus(l))