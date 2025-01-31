# Найти колво пар чисел A, B, таких что B - A > k
nums = [1, 3, 3, 4, 5, 6]
def cntPairs(nums):
    r = 0
    k = 2
    cntPairs = 0
    for i in range(len(nums)):
        while r < len(nums) and nums[r] - nums[i] <= k:
                r += 1
        print(r, len(nums) - r)
        cntPairs += len(nums) - r
    print(cntPairs)    
cntPairs(nums)

