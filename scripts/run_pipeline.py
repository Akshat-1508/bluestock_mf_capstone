"""
Master execution script
"""

import subprocess
import sys

print("Running ETL Pipeline...")
subprocess.run(
    [sys.executable, "scripts/etl_pipeline.py"]
)

print("Running Recommender...")
subprocess.run(
    [sys.executable, "scripts/recommender.py"]
)

print("Pipeline Complete")