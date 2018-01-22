import math

digit_sum_primes_gt_1M = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
test = primes[-1] + 2

while len(digit_sum_primes_gt_1M) < 2:
    test_sqrt = math.sqrt(test)
    test_is_prime = True
    for i in xrange(len(primes)):
        if primes[i] > test_sqrt:
            break

        if test % primes[i] == 0:
            test_is_prime = False
            break

    if test_is_prime:
        primes.append(test)
        if test > 1000000:
            digit_sum = sum(int(i) for i in str(test))
            if digit_sum in primes:
                print test
                digit_sum_primes_gt_1M.append(test)
    test += 2
