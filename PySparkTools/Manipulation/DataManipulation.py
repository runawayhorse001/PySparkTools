from functools import reduce
from pyspark.sql import DataFrame


def unionAll(*dfs):
    """
    data frame union for two or multiple data frames.
    reference: https://stackoverflow.com/questions/
               33743978/spark-union-of-multiple-rdds
    """
    return reduce(DataFrame.unionAll, dfs)