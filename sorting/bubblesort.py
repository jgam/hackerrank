def countSwaps(a):
    num_swap = 0
    if a == sorted(a):
        print('Array is sorted in', num_swap, 'swaps.')
        print('First Element:', a[0])
        print('Last Element:', a[-1])
        return 0
    else:
        for i in range(1,len(a)):
            for j in range(len(a)-i):
                if a[j] > a[j+1]:
                    first_num, second_num = a[j+1], a[j]
                    a[j+1] = second_num
                    a[j] = first_num
                    num_swap += 1
    print('Array is sorted in', num_swap, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])