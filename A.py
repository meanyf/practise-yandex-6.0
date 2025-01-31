# A. Префиксные суммы
n = 5
numbers = [10, -4, 5, 0, 2]

def makeprefix(nums):
    if not nums:
        print(arr)
    arr = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        arr[i] = arr[i - 1] + nums[i - 1]
    del arr[0] 
    print(*arr)

makeprefix(numbers)
