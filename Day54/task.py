import time

def speed_calc_decorator(function):
    def any_function():
        start_time = time.time()
        function()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed time: ", elapsed_time)
    return any_function


@speed_calc_decorator
def fast_func():
    for number in range(1000000):
        return number

@speed_calc_decorator
def slow_func():
    for number in range(100000000000):
        return number


fast_func()
slow_func()