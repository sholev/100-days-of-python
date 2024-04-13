import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(func):
    def wrapper_function():
        start_time = time.time()
        func()
        finish_time = time.time()
        print(f"{func.__name__} run speed: {finish_time - start_time}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        result = i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        result = i * i


fast_function()
slow_function()
