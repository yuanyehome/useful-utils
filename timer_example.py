import logging
import time

from timer import timer, get_timer

# default timer's logging level is logging.DEBUG
# so timer would print nothing if logging level is logging.INFO or higher
logging.basicConfig(level=logging.DEBUG)

# or you can change default timer's logging level
timer.set_level(logging.DEBUG)

# also you can get a timer with custom logging level with get_timer(level)
warning_timer = get_timer(logging.WARNING)


# explicit the timer's name and it's time unit
@timer('function:add', unit='s')
def add(a, b):
    time.sleep(.1)
    return a + b


# function name is timer's name for default
@timer
def sub(a, b):
    time.sleep(.1)
    return a - b


if __name__ == '__main__':
    # 'timer' would be timer's name by default
    with timer('time.sleep(2)') as t:
        print(3)
        time.sleep(1)
        print(f'after time.sleep(1) once, t.elapse = {t.elapse}')
        time.sleep(1)
        print(f'after time.sleep(1) twice, t.elapse = {t.elapse}')
    print(f'after with, t.elapse = {t.elapse}')

    with warning_timer('test'):
       pass

    print(add(1, 1))
    print(sub(2, 1))
