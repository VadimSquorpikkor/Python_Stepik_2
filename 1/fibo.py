def fibo_slow(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibo_slow(n - 1) + fibo_slow(n - 2)


# print(fibo_slow(int(input())))


def fibo_fast(n):
    fn = 1
    f1 = 0  # yes, i know that first fibo is 1. when work, function return right fibo
    f2 = 1
    for i in range(n - 1):
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fn

print(fibo_fast(int(input())))
