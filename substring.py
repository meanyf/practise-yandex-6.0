string = "abacccda"
k = 2
r = 0
d = dict()
length = 0
for i, char in enumerate(string):
    while r < len(string) and d.get(string[r], 0) < k:
        d[string[r]] = d[string[r]] + 1 if string[r] in d else 1
        r += 1
    length = max(length, r - i)
    d[char] = d[char] - 1 if string[i] in d else 0
    # print("char", char)
    # print(d)


print(length)



