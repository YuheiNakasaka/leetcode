N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

maxinum = max(nums)
maxinum2 = -1
for i in range(N):
    if nums[i] == maxinum:
        if maxinum2 == -1:
            maxinum2 = max(nums[0:i] + nums[i+1:])
        print(maxinum2)
    else:
        print(maxinum)