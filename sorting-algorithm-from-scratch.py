numbers = [12, 4, 5, 98, 3, 6, 12, 4, 6, 5, 60, 34]
sorted = []

def sort_func(nums):
    values = {}
    data = set(nums)
    for i in data:
        occurence = 0
        for k in nums:
            if i == k:
                occurence += 1
        values[i] = occurence
    print(values)
    values_copy = [i for i in values.keys()]
    print(values_copy)
    for n in nums:
        for num in values_copy:
            res = all(num <= i for i in values_copy)
            if res:
                values_copy.remove(num)
                if num not in values_copy:
                    for l in range(values[num]):
                        sorted.append(num)


    print(sorted)


sort_func(numbers)