from pyspark.sql import SparkSession

# Initialize Spark session

spark = SparkSession.builder.appName("HelloWorld").getOrCreate()

# Sample data
data = ["hello world", "hello Spark", "Apache Spark is awesome"]

# Parallelize data into an RDD
rdd = spark.sparkContext.parallelize(data)

# Word count example
word_counts = (
        rdd.flatMap(lambda line: line.split(" "))  # Split lines into words
        .map(lambda word: (word, 1))               # Create pairs (word, 1)
        .reduceByKey(lambda a, b: a + b)           # Aggregate counts by key
        )

# Collect and print the results
print("Word Counts:")
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop Spark session
spark.stop()
