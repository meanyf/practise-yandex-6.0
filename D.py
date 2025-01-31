# D. Лучший отдых

k = 2
nums = [3, 8, 5, 7, 1, 2, 4, 9, 6]
nums = [1, 4, 7, 10]
n = len(nums)

nums.sort()
print(nums)

d = dict()
r = 0
cnt = 0
for i in range(n):
    while r < n and nums[r] - nums[i] <= k:
        r += 1
    if r < n and nums[r] - nums[i] > k :
        cnt += 2   
      

print(cnt)


# numbers = [0, 5, 2,2, 4, -2, -1, +1, 6, 3]
# numbers = [1, 1, 1, 1]

# s = set()

# del numbers[0]

# ex_elem = 0
# for num in numbers:
#     if abs(num) < 3:
#         s.add(abs(num))
#     else:
#         ex_elem = 1
# print(len(s) + ex_elem)


