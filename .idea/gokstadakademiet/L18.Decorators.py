
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} blir kalt med argumenter {args} og nøkkelord {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add(a, b):
    return a + b

result = add(3, 4)
print("Result:", result)



print("-----------------------------------------------------------------------")

import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        resultat = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} tok {end_time - start_time} sekunder å kjøre")
        return resultat
    return  wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    #print(5+5)          #uten å bruke time.sleep(2)
    print("Hei alle sammen!")

slow_function()

