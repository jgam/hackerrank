#The mathematics, the fibonacci series is defined by the following recurrence relation:
#F(0) ＝ 0 ...... F(n) ＝ F(nー１）＋F(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

print(fibonacci(6))