nums = [5, 3,  8, 1, 4, 6, ]
def makeprefix(nums):
    arr = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        arr[i] = arr[i - 1] + nums[i - 1]
    print(arr)
    return arr

def rsq(prefix, l, r):
    result = prefix[r] - prefix[l]
    print(result)
    return result

arr = makeprefix(nums)
rsq(arr, 2, 5)