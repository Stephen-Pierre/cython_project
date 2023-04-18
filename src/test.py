import timeit


def test():
    print(timeit.timeit(stmt="fib_py(n=100000)",
                        setup="from fib_py import fib_py", number=10))


def test1():
    from fib_cy import fibo_cy
    print(fibo_cy(100000))
    print(timeit.timeit(stmt="fibo_cy(100000)",
                        setup="from fib_cy import fibo_cy", number=10))


if __name__ == '__main__':
    test()
    test1()