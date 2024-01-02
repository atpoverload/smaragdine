""" A cli to process globs of smaragdine proto files. """
import os

from argparse import ArgumentParser
from zipfile import ZipFile

from smaragdine.energy import compute_footprint
from smaragdine.protos.sample_pb2 import DataSet


def parse_args():
    """ Parses virtualization arguments. """
    parser = ArgumentParser()
    parser.add_argument(
        dest='files',
        nargs='*',
        default=None,
        help='files to process',
    )
    parser.add_argument(
        '-o',
        '--output_dir',
        dest='output',
        default=None,
        help='directory to write the processed data to',
    )
    return parser.parse_args()


def main():
    args = parse_args()
    for file in args.files:
        with open(file, 'rb') as f:
            data = DataSet()
            data.ParseFromString(f.read())

        if args.output:
            if os.path.exists(args.output) and not os.path.isdir(args.output):
                raise RuntimeError(
                    'output target {} already exists and is not a directory; aborting'.format(args.output))
            elif not os.path.exists(args.output):
                os.makedirs(args.output)

            path = os.path.join(args.output, os.path.splitext(
                os.path.basename(file))[0]) + '.zip'
        else:
            path = os.path.splitext(file)[0] + '.zip'
        print('virtualizing data from {}'.format(file))
        footprints = compute_footprint(data)

        # TODO: this only spits out a single file. we should be able to write
        #   multiple files to the archive, but maybe not with pandas
        with ZipFile(path, 'w') as archive:
            for key in footprints:
                archive.writestr('{}.csv'.format(
                    key), footprints[key].to_csv())


if __name__ == '__main__':
    main()
