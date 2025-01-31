list1 = []
list2 = [1, 2, 4]
merged = []
l = r = 0
while l < len(list1) or r < len(list2):
    if l != len(list1) and (r == len(list2) or list1[l] <= list2[r]):
        merged.append(list1[l])
        l += 1
    else:
        merged.append(list2[r])
        r +=1
print(merged)