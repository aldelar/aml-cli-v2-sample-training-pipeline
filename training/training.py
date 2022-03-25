# imports
import os
import argparse
import pandas as pd
import joblib

# main
def main(args):
    df = pd.read_csv(args.training_dataset)
    # train the model...
    model = 0
    joblib.dump(model, args.model_path)

# parse arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--training_dataset", type=str)
    parser.add_argument("--model_path", type=str)
    args = parser.parse_args()
    return args

# run script
if __name__ == "__main__":
    main(parse_args())