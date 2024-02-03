import json
import os
import zipfile

from argparse import ArgumentParser

import numpy as np
import pandas as pd

# from tqdm import tqdm

from smaragdine.tensor import get_flow, flatten_flow, generate_footprint


def parse_args():
    """ Parses accounting arguments. """
    parser = ArgumentParser()
    parser.add_argument(
        dest='flow',
        help='path to flow trace',
    )
    parser.add_argument(
        dest='power',
        help='path to power trace',
    )
    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.flow) as f:
        flow = flatten_flow(get_flow(json.load(f)))

    source = args.power.split(os.path.sep)[-1].split('-')[0]
    # some ugly magic to create a dict<device, dict<timestamp, power>>
    power = pd.read_csv(args.power, parse_dates=['timestamp'])
    power['ts'] = pd.to_datetime(power.timestamp).astype(np.int64) // 1000

    footprint = []
    if source == 'nvml':
        for device, df in power.groupby('device_index'):
            f = flow[f'GPU:{device}']
            footprint.append(generate_footprint(
                f, df.set_index('ts').power.to_dict()))
    else:
        for device, df in power.groupby('socket'):
            f = flow[f'CPU:{device}']
            footprint.append(generate_footprint(
                f, df.set_index('ts').power.to_dict()))
    print(footprint)


if __name__ == '__main__':
    main()
