from random import randint
#  Generate 1000 random numbers between 0 and 100000
numbers = [randint(0, 100000) for i in range(1000)]
#  create an empty list to store the sorted values
sorted = []


def sort_func(nums):
    #  create an empty dictionary to store each unique value
    #  and the number of times it occurs
    values = {}
    #  store the values in a set to get each unique value
    data = set(nums)
    #  Getting the number of times a value occurs
    for i in data:
        occurrence = 0
        for k in nums:
            if i == k:
                occurrence += 1
        values[i] = occurrence
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