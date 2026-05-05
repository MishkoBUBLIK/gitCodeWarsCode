array = [
    [1,  2,  3,  4,  5,  6,  7],
    [8,  9,  10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42],
    [43, 44, 45, 46, 47, 48, 49]
]
# My solution

def snail(array):
    snail_array = []
    while array:
        for num in array[0]:
            snail_array.append(num)
        array.remove(array[0])

        for i in range(0, len(array) - 1):
            number = array[i][-1]
            snail_array.append(number)
            array[i].pop()

        if array:
            for num in reversed(array[-1]):
                snail_array.append(num)
            array.remove(array[-1])
        else:
            break

        for j in range(len(array) - 1, 0, -1):
            snail_array.append(array[j][0])
            array[j].pop(0)
    return snail_array

print(snail(array))
