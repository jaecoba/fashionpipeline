#!/bin/bash

# Activate virtual environment (if needed)
source /Users/jadajar/fashionanalysis/venv/bin/activate

# Step 1: Fetch Data
echo "Fetching data..."
python3 /Users/jadajar/fashionanalysis/scripts/fetch_data.py
if [ $? -ne 0 ]; then
    echo "fetch_data.py failed!" >> /Users/jadajar/fashionanalysis/logs/pipeline.log
    exit 1
fi

# Step 2: Transform Data
echo "Transforming data..."
python3 /Users/jadajar/fashionanalysis/scripts/transform_data.py
if [ $? -ne 0 ]; then
    echo "transform_data.py failed!" >> /Users/jadajar/fashionanalysis/logs/pipeline.log
    exit 1
fi

# Step 3: Load Data to AWS RDS
echo "Loading data to RDS..."
python3 /Users/jadajar/fashionanalysis/scripts/load_data.py
if [ $? -ne 0 ]; then
    echo "load_data.py failed!" >> /Users/jadajar/fashionanalysis/logs/pipeline.log
    exit 1
fi

echo "Pipeline completed successfully!" >> /Users/jadajar/fashionanalysis/logs/pipeline.log
