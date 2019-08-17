N = int(input())
h = {}
for i in range(N):
    restaurant, score = list(input().split())
    item = h.get(restaurant, [])
    item.append([int(score), i+1])
    h[restaurant] = sorted(item,key=lambda x: -x[0])

for key in sorted(h.keys()):
    for item in h[key]:
        print(item[1])
