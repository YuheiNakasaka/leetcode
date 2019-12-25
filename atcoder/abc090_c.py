# あるマスの接する面・点の数が偶数の時、そのマスは裏になる
N,M = list(map(int, input().split()))

if N == 1 or M == 1:
    # N,Mのどちらかが1の時は話が変わる
    print(abs(N * M - 2))
else:
    # 四隅でも外周でも無い内側のマス
    print(N * M - (4 + (N - 2) * 2 + (M - 2) * 2))