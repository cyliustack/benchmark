from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession
from pyspark.ml.stat import Correlation
import operator
import pyspark

def mldemo():

    spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    data = [(Vectors.sparse(4, [(0, 1.0), (3, -2.0)]),),
            (Vectors.dense([4.0, 5.0, 0.0, 3.0]),),
            (Vectors.dense([6.0, 7.0, 0.0, 8.0]),),
            (Vectors.sparse(4, [(0, 9.0), (3, 1.0)]),)]
    df = spark.createDataFrame(data, ["features"])
    
    r1 = Correlation.corr(df, "features").head()
    print("Pearson correlation matrix:\n" + str(r1[0]))
    
    r2 = Correlation.corr(df, "features", "spearman").head()
    print("Spearman correlation matrix:\n" + str(r2[0]))

def main():
    #Intialize a spark context
    with pyspark.SparkContext("local", "PySparkWordCount") as sc:
        #Get a RDD containing lines from this script file  
        lines = sc.textFile(__file__)
        #Split each line into words and assign a frequency of 1 to each word
        words = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))
        #count the frequency for words
        counts = words.reduceByKey(operator.add)
        #Sort the counts in descending order based on the word frequency
        sorted_counts =  counts.sortBy(lambda x: x[1], False)
        #Get an iterator over the counts to print a word and its frequency
        for word,count in sorted_counts.toLocalIterator():
            print(u"{} --> {}".format(word, count))

if __name__ == "__main__":
    main()
    mldemo()
