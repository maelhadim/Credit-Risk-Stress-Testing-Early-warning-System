# Generated from: config.ipynb
# Converted at: 2026-01-04T17:02:32.863Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

RANDOM_STATE = 42

TARGET_COL = "default.payment.next.month"

RAW_DATA_PATH = "default of credit card clients.csv"
PROCESSED_TRAIN_PATH = "data/processed/train.csv"
PROCESSED_TEST_PATH = "data/processed/test.csv"

TEST_SIZE = 0.2
N_SPLITS_CV = 5