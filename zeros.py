nums = [0, 0, 1, 1, 0]

def makeprefix(nums):
    arr = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            arr[i] = arr[i - 1] + 1 
        else:
            arr[i] = arr[i - 1]
    print(arr)   
    return arr     

def rsq(prefix, l, r):
    result = prefix[r] - prefix[l]
    print(result)
    return result

arr = makeprefix(nums)

rsq(arr, 0, 5)

