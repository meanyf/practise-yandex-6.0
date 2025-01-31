# B. Сумма номеров
# n, k = list(map(int, input().split()))
# numbers = list(map(int, input().split()))
numbers = []
n = len(numbers)
k = 1


def makeprefix(nums):
    if not nums:
        return []
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = arr[i - 1] + nums[i - 1]
    return arr

def rsq(prefix, l, r):
    result = prefix[r] - prefix[l]
    return result

arr = makeprefix(numbers)
r = 0
cnt = 0

for i in range(n):
    while r < n + 1 and rsq(arr, i, r) <= k:
        if rsq(arr, i, r) == k:
            cnt += 1
        r += 1

print(cnt)


        





