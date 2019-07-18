nums = list(input())


A = [0, 1]
B = [0, 1]
C = [0, 1]
ops = {
  0: "+",
  1: "-"
}
total = 0
res = ''
for a in range(2):
    for b in range(2):
        for c in range(2):
            if a == 0:
                total = int(nums[0]) + int(nums[1])
            else:
                total = int(nums[0]) - int(nums[1])
            if b == 0:
                total = total + int(nums[2])
            else:
                total = total - int(nums[2])
            if c == 0:
                total = total + int(nums[3])
            else:
                total = total - int(nums[3])
            if total == 7:
                res = nums[0] + ops[a] + nums[1] + ops[b] + nums[2] + ops[c] + nums[3] + "=7"

print(res)
