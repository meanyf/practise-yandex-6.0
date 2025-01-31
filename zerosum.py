# Найти колво отрезков с нулевой суммой
nums = [1, 2, -3, 4, -2, 1, -3, 0]
def makeprefix(nums):
    arr = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        arr[i] = arr[i - 1] + nums[i - 1]
    print(arr)
    return arr

def formula(N):
    result = N*(N - 1)/2
    print(result)
    return result

def countSegments(prefixsum):
    d = dict()
    sum = 0
    for num in prefixsum:
        d[num] = d[num] + 1 if num in d else 1
    for cntValue in d.values():
        if cntValue > 1:
            sum += formula(cntValue)       
    print(d)
    print(sum)
    return(sum)


prefixsum = makeprefix(nums)
countSegments(prefixsum)

def test_makeprefix():
    assert makeprefix([1, 2, -3, 4, -2, 1, -3, 0]) == [0, 1, 3, 0, 4, 2, 3, 0, 0], "Ошибка в makeprefix"
    assert makeprefix([0, 0, 0, 0]) == [0, 0, 0, 0, 0], "Ошибка в makeprefix"
    assert makeprefix([5]) == [0, 5], "Ошибка в makeprefix"
    print("Тесты для makeprefix прошли успешно!")

test_makeprefix()