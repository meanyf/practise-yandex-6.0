numbers = [1, 3, 5, 8]
n = len(numbers)
r = 4

right = 0
cnt = 0

for i in range(n):
    while right < n and numbers[right] - numbers[i] <= r:
        right += 1
    cnt += n - right
print(cnt)