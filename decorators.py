from datetime import datetime
from time import sleep

def timing(func):
    def modified(*args, **kwargs):
        start_time = datetime.now();
        output = func(*args, **kwargs)
        print(f'{func.__name__} took {datetime.now() - start_time}')
        return output
    return modified

def debugging(func):
    def modified(*args, **kwargs):
        starttime = datetime.now
        output = func(*args, **kwargs)
        print(f'{func.__name__} took {datetime.now() - start_time}')
        return output
    return modified


@debugging
def sleepy(x, foo=None):
    sleep(1)
    return 3


@timing
def sleepy(x, foo=None):
    sleep(1)
    return 3

