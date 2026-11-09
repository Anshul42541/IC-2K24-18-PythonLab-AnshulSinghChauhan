
import time
import random

# Naive approach

def naive(arr, k):
    sums = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sums.append(arr[i] + arr[j])

    sums.sort()

    return sums[k - 1]


# Optimized approach

def count_pairs(arr, value):
    count = 0
    j = len(arr) - 1

    for i in range(len(arr)):

        while i < j and arr[i] + arr[j] > value:
            j -= 1

        count += j - i

    return count


def optimized(arr, k):
    arr.sort()

    low = arr[0] + arr[1]
    high = arr[-1] + arr[-2]

    while low < high:
        mid = (low + high) // 2

        if count_pairs(arr, mid) >= k:
            high = mid
        else:
            low = mid + 1

    return low


# Testing

print("Naive:", naive([1, 3, 5, 7], 1))
print("Optimized:", optimized([1, 3, 5, 7], 1))

print("Naive:", naive([1, 3, 5, 7], 3))
print("Optimized:", optimized([1, 3, 5, 7], 3))

print("Naive:", naive([1, 3, 5, 7], 6))
print("Optimized:", optimized([1, 3, 5, 7], 6))

print("Naive:", naive([4, 4, 4], 1))
print("Optimized:", optimized([4, 4, 4], 1))

print("Naive:", naive([2, 5, 10], 2))
print("Optimized:", optimized([2, 5, 10], 2))


# Performance testing

random.seed(42)

N = 5000
arr = [random.randint(1, 100000) for _ in range(N)]
K = 1000000

start = time.time()
result1 = naive(arr, K)
time1 = time.time() - start

print("\nNaive result:", result1)
print("Naive time:", time1, "seconds")


start = time.time()
result2 = optimized(arr.copy(), K)
time2 = time.time() - start

print("\nOptimized result:", result2)
print("Optimized time:", time2, "seconds")


# Final comparison

print("\nExecution Time Comparison")
print("Naive:", time1, "seconds")
print("Optimized:", time2, "seconds")
