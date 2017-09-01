from pyspark.sql import SparkSession
spark = SparkSession \
        .builder \
        .appName("Python Spark Data Frame Union Demo") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()


from PySparkTools.Manipulation.dataManipulation import unionAll