# imports
import os
import argparse
import joblib

# AML imports
from azureml.core import Model, Workspace

# main
def main(args):
    # get AML workspace
    if args.run_mode =='remote':
        workspace = Run.get_context().experiment.workspace
    else:
        workspace = Workspace.from_config()
    # load model
    model = joblib.load(args.model_path)
    # evaluate the model... to log metrics about its performance when registering
    # register the model (no performance metrics are logged here yet)
    Model.register(workspace,model_path=args.model_path,model_name=args.model_name)

# parse arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str)
    args = parser.parse_args()
    return args

# run script
if __name__ == "__main__":
    main(parse_args(),run_id)