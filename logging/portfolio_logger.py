import logging
from functools import wraps
import os
import sys
import datetime as dt
import time

def analytics_logger(func):
    '''
    logging function for analytics engine


    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        config_fpath = os.getcwd()
        config_fname = r'analytics.log'

        logger = logging.getLogger('analytics_logger')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(os.path.join(config_fpath, config_fname))
        fh.setLevel(logging.DEBUG)
        logger.addHandler(fh)
        today = dt.date.today().strftime('%y-%m-%d')
        payload = f'{today}: Function {func.__name__} '

        #with read_yaml(config_fpath, config_fname) as config:

        #context manage config to analytics
        try:
            t0 = time.time()
            res = func(*args, **kwargs)
            run_time = time.time() - t0
            payload += f'took {run_time} to run'
            logger.info(payload)

        except Exception as err:
            #basic for the moment but lets run with it...
            payload += f'was unable to run. Error handled: {err}'
            logger.info(payload)
            res = -1

        return res



    return wrapper

@analytics_logger
def easy_function(a, b):
    print(a)
    print(b)
    return a * b / ((a + b) * b % a)

def main():
    print(easy_function(10, 21))



if __name__ == '__main__':
    main()
