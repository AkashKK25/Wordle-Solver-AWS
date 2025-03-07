"""
AWS Configuration for Wordle Solver Application
Note: This file is for documentation purposes only in the current deployment.
In an AWS deployment, these values would be set as environment variables.

AWS Resources:
- S3 Bucket: For storing word dictionaries
- CloudWatch: For application logging and monitoring
- Parameter Store: For secure configuration storage
"""

# AWS region
AWS_REGION = "us-east-1"

# S3 bucket details
S3_BUCKET_NAME = "wordle-solver-dictionaries"
S3_COMMON_DICT_KEY = "WORDLE_Dictionary.txt"
S3_RARE_DICT_KEY = "rare_words.txt"

# CloudWatch configuration
LOG_GROUP_NAME = "wordle-solver-logs"
METRICS_NAMESPACE = "WordleSolverMetrics"

# Batch size for updating metrics
METRICS_BATCH_SIZE = 100