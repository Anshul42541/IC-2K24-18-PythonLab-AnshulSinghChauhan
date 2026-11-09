
import time
import random

# Naive approach

def naive(arr, target):
    count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1

    return count


# Optimized approach

def optimized(arr, target):
    seen = {}
    count = 0

    for num in arr:
        required = target - num

        if required in seen:
            count += seen[required]

        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    return count


# Testing

print("Naive:", naive([2, 7, 11, 15], 9))
print("Optimized:", optimized([2, 7, 11, 15], 9))

print("Naive:", naive([1, 1, 1], 2))
print("Optimized:", optimized([1, 1, 1], 2))


# Performance testing

random.seed(42)

N = 5000
arr = [random.randint(1, 20000) for _ in range(N)]
target = 20000

start = time.time()
print("\nNaive result:", naive(arr, target))
print("Naive time:", time.time() - start)

start = time.time()
print("Optimized result:", optimized(arr, target))
print("Optimized time:", time.time() - start)


# N = 50000

N = 50000
arr = [random.randint(1, 20000) for _ in range(N)]

start = time.time()
print("\nNaive result:", naive(arr, target))
print("Naive time:", time.time() - start)

start = time.time()
print("Optimized result:", optimized(arr, target))
print("Optimized time:", time.time() - start)
