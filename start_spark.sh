#!/bin/bash
echo "🚀 Starting Spark in Codespace..."

# Activate venv
source .venv/bin/activate

# Install dependencies if needed
pip install -q pyspark findspark

# Run Python script
python -c "
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('QuickStart').master('local[*]').getOrCreate()
spark.sparkContext.setLogLevel('WARN')
print(f'✅ Spark {spark.version} is ready!')
print('📊 Spark UI: http://localhost:4040')
df = spark.range(10)
print('✅ Test data created:')
df.show()
spark.stop()
"