import pandas as pd
import multiprocessing
from multiprocessing import Pool
import time
import statistics
from collections import namedtuple

FILENAME = 'maori-statistics.csv'

def time_it(fn):

    """This is a decorator used for timing functions."""

    def wrapper_function(*args, **kwargs):
        begin = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print('Function {0} executed in {1} s'.format(fn.__name__, end - begin))
        return result
    
    return wrapper_function

# @time_it -> mapping does not work with decorators
def count_properties(values: list[int]) -> tuple:

    """This funcitons calculates basic properties of a list of integers, such as min, max and mean value."""

    max_val = max(values)
    min_val = min(values)
    mean_val = round(sum(values)/len(values), 2)
    std_dev = round(statistics.stdev(values), 2)
    variance = round(statistics.variance(values), 2)

    return (min_val, max_val, mean_val, std_dev, variance)

if __name__ == '__main__':

    # read CSV file and extract a list containing integer values of transactions
    df = pd.read_csv(FILENAME)
    values = [int(record) for record in df.Value if record.isdigit()]

    # create named tuple containing basic properties of a list of integers
    Properties = namedtuple('Properties', 'min_value max_value mean_value standard_deviaton variance')

    # iterate over the number of CPU cores
    for i in range(1, multiprocessing.cpu_count() + 1):

        pool = Pool(i)

        begin = time.perf_counter()
        # map count_properties; it requires an iterable, so values wrapped are into an iterable (single-element tuple in this case)
        # otherwise count_properties function would be performed on every element of values list, causing errors
        results = pool.map(count_properties, (values,))
        end = time.perf_counter()

        pool.close()
        pool.join()

        print('Function {0} executed in {1} s'.format(count_properties.__name__, end - begin))
        print('Number of CPU cores used: {0}'.format(i))
        print('*' * 10)

    # results contain an iterable with one element (tuple), so we extract the first element and unpack it into a named tuple
    properties = Properties(*results[0])
  
    for field in properties._fields:
        value = getattr(properties, field)
        print('{0}: {1}'.format(field, value))
