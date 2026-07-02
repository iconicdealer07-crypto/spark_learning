from pyspark.sql import SparkSession
import time
import os

print("🚀 Starting Spark with UI...")

# Create Spark session
spark = SparkSession.builder \
    .appName("SparkUILearning") \
    .master("local[*]") \
    .config("spark.ui.enabled", "true") \
    .config("spark.ui.port", "4041") \
    .config("spark.ui.bindAddress", "0.0.0.0") \
    .config("spark.driver.host", "0.0.0.0") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()

# Set log level
spark.sparkContext.setLogLevel("WARN")

# Create some data to make UI interesting
print("📊 Creating test data...")

# Create sample data
data = [(f"User{i}", i%5, i*10) for i in range(1000)]
df = spark.createDataFrame(data, ["name", "group", "score"])

# Perform operations
print("🔄 Running analysis...")
result = df.groupBy("group").agg(
    {"score": "avg", "score": "max", "score": "min"}
).collect()

print("✅ Data loaded and analyzed")

# Cache some data to show in UI
df.cache().count()

# Show the URL
ui_url = spark.sparkContext.uiWebUrl
print(f"\n✅ Spark {spark.version} is running!")
print(f"📊 Spark UI URL: {ui_url}")
print(f"📊 Try opening: http://localhost:4041")
print("\n💡 Keep this terminal running")
print("💡 Open a NEW terminal for other commands")
print("\n⏳ Press Ctrl+C to stop Spark\n")

# Keep session alive with periodic activity
try:
    while True:
        time.sleep(30)
        # Keep session active
        spark.sql("SELECT 1").collect()
        print("⏳ Spark session active...")
except KeyboardInterrupt:
    print("\n🛑 Stopping Spark...")
    spark.stop()
    print("✅ Spark stopped")
