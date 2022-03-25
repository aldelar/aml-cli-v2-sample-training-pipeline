# imports
import os
import argparse
import pandas as pd

# main
def main(args):
    df = pd.read_csv(args.raw_dataset)
    # assume some feature engineering here...
    df.to_csv(args.training_dataset, index=False)

# parse arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw_dataset", type=str)
    parser.add_argument("--training_dataset", type=str)
    args = parser.parse_args()
    return args

# run script
if __name__ == "__main__":
    main(parse_args())