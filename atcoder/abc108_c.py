# Kが奇数の時はa,b,cが全てKの倍数
# Kが偶数の時はa,b,cが全てmod(K)=0 となるか mod(K)=K/2となる
# なのでそれらを数え上げて3乗するだけ
N, K = list(map(int, input().split()))

if K % 2 == 0:
    l1 = 0
    l2 = 0
    for i in range(1, N+1):
        if i % K == 0:
            l1 += 1
        if i % K == (K / 2):
            l2 += 1
    print(l1 ** 3 + l2 ** 3)
else:
    l1 = 0
    for i in range(1, N+1):
        if i % K == 0:
            l1 += 1
    print(l1 ** 3)
