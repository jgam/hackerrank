def pairs(k, arr):
    numbers = set()
    count = 0
    for n in arr:
        if n + k in numbers:
            count += 1
        if n - k in numbers:
            count += 1
        numbers.add(n)
    return count