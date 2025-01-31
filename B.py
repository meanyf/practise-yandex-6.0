# B. Сумма номеров
# n, k = list(map(int, input().split()))
# numbers = list(map(int, input().split()))
numbers = [17, 7, 10, 7, 10]
n = len(numbers)
k = 17 

# two pointers

r = 0
sum = 0
cnt = 0
for i in range(n):
    while r < n and sum < k:
        sum += numbers[r]
        r += 1
    if sum >= k:
        if sum == k:
            cnt += 1
        sum -= numbers[i]
print(cnt)

# prefix sum 

# def makeprefix(nums):
#     if not nums:
#         return []
#     arr = [0] * (n + 1)
#     for i in range(1, n + 1):
#         arr[i] = arr[i - 1] + nums[i - 1]
#     return arr

# def rsq(prefix, l, r):
#     result = prefix[r] - prefix[l]
#     return result

# arr = makeprefix(numbers)
# r = 0
# cnt = 0

# print(arr)
# for i in range(n):
#     while r < n + 1 and rsq(arr, i, r) <= k:
#         if rsq(arr, i, r) == k:
#             cnt += 1
#         r += 1

# print(cnt)


        





