from pyspark.sql import SparkSession
spark = SparkSession \
        .builder \
        .appName("Python Spark Data Frame Union Demo") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()


from PySparkTools.Manipulation.DataManipulation import unionAll

df1 = spark.createDataFrame([(1, "data1"), (2, "data2")], ("ID", "Value"))
df2 = spark.createDataFrame([(3, "data3"), (4, "data4")], ("ID", "Value"))
df3 = spark.createDataFrame([(5, "data5"), (6, "data6")], ("ID", "Value"))

df1.show()
df2.show()
df3.show()


df = unionAll(df1, df2, df3)
df.show()

