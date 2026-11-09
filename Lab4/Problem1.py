
import time
import math

# ---------------------------------
# 1. NAIVE VERSION
# ---------------------------------

def naive_prime_sum(N):

    total = 0

    for num in range(2, N):

        is_prime = True

        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            total += num

    return total


# ---------------------------------
# 2. SMALLER BOUND OPTIMIZATION
# ---------------------------------

def optimized_prime_sum(N):

    total = 0

    for num in range(2, N):

        is_prime = True

        for i in range(2, math.isqrt(num) + 1):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            total += num

    return total


# ---------------------------------
# 3. SIEVE OF ERATOSTHENES
# ---------------------------------

def sieve_prime_sum(N):

    if N <= 2:
        return 0

    is_prime = [True] * N

    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, math.isqrt(N - 1) + 1):

        if is_prime[i]:

            for j in range(i * i, N, i):
                is_prime[j] = False

    total = 0

    for i in range(N):

        if is_prime[i]:
            total += i

    return total


# ---------------------------------
# 4. TEST CASES
# ---------------------------------

test_cases = [10, 2, 3, 20, 100]

print("========== CORRECTNESS TESTING ==========")

for N in test_cases:

    print("\nN =", N)

    print("Naive Sum:", naive_prime_sum(N))

    print("Smaller Bound Sum:", optimized_prime_sum(N))

    print("Sieve Sum:", sieve_prime_sum(N))


# ---------------------------------
# 5. PERFORMANCE TESTING
# ---------------------------------

N = 2000000

print("\n========== PERFORMANCE TESTING ==========")

# Naive Version
start = time.time()
result1 = naive_prime_sum(N)
time1 = time.time() - start

print("\nNaive Version")
print("Sum:", result1)
print("Time Taken:", time1, "seconds")


# Smaller Bound Version
start = time.time()
result2 = optimized_prime_sum(N)
time2 = time.time() - start

print("\nSmaller Bound Version")
print("Sum:", result2)
print("Time Taken:", time2, "seconds")


# Sieve Version
start = time.time()
result3 = sieve_prime_sum(N)
time3 = time.time() - start

print("\nSieve Version")
print("Sum:", result3)
print("Time Taken:", time3, "seconds")


# ---------------------------------
# 6. COMPARISON
# ---------------------------------

print("\n========== FINAL COMPARISON ==========")

print("Naive:", time1, "seconds")

print("Smaller Bound:", time2, "seconds")

print("Sieve:", time3, "seconds")
