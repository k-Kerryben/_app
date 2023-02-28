from random import randint

numbers = [randint(0, 1000000) for i in range(1000)]
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
    values_copy = [i for i in values.keys()]

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