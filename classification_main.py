import traceback
import argparse
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split

classes = 5
data_size = 1920 * 1080 * 3


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=str)
    args = parser.parse_args()

    return args

def model_training


def main(args):
    pass


if __name__ == '__main__':
    main(parse_args())
