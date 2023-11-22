import random
import time


# naive search
def naive_search(target, arr):
    for i in arr:
        if i == target:
            return True
    return False


def binary_search(target, arr, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    if high < low:
        return -1
    midpoint = (low+high) // 2

    if arr[midpoint] == target:
        return 1
    elif arr[midpoint] < target:
        return binary_search(target, arr, low, midpoint-1)
    else:
        return binary_search(target, arr, midpoint+1, high)


if __name__ == "__main__":
    sorted_list = set()

    for i in range(10000):
        sorted_list.add(random.randint(-3*10000, 3*10000))

    sorted_list = sorted(list(sorted_list))

    # naive search
    start = time.time()
    for index, target in enumerate(sorted_list):
        target = sorted_list[random.randint(0, index)]
        naive_search(target, sorted_list)
    end = time.time()
    naive_time = end - start

    # binary search
    start1 = time.time()
    for index, target in enumerate(sorted_list):
        target = sorted_list[random.randint(0, index)]
        binary_search(target, sorted_list)
    end1 = time.time()

    binary_time = end1 - start1

    print(naive_time)
    print(binary_time)

    # arr = [1,2,3,4]
    # tar = 4
    # print(binary_search(tar, arr))

    # print("hello")

