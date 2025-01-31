# a + b >= c
nums = [1, 100]

bestsum = 0
nowsum = 0
last = 0

for i in range(len(nums)):
    while last < len(nums) and (nums[i] + nums[i + 1] >= nums[last]):
        nowsum += nums[last]
        last += 1
    bestsum = max(nowsum, bestsum)
    print(nowsum)
    nowsum -= nums[i]
    
