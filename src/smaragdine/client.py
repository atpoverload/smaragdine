""" a client that can talk to an smaragdine sampler. """
from argparse import ArgumentParser
from os import getpid
from time import sleep

from smaragdine.sampler import SmaragdineSampler


def parse_args():
    """ Parses client-side arguments. """
    parser = ArgumentParser()
    parser.add_argument(
        dest='command',
        choices=['start', 'stop', 'read'],
        help='request to make',
    )
    parser.add_argument(
        '--pid',
        dest='pid',
        type=int,
        default=getpid(),
        help='pid to be monitored',
    )
    parser.add_argument(
        '--addr',
        dest='addr',
        type=str,
        default='[::1]:50051',
        help='address of the smaragdine server',
    )
    return parser.parse_args()


def main():
    args = parse_args()

    client = SmaragdineSampler(args.addr)
    if args.command == 'start':
        if args.pid < 0:
            raise Exception(
                'invalid pid to monitor ({})'.format(args.pid))
        client.start(args.pid)
    elif args.command == 'stop':
        client.stop()
    elif args.command == 'read':
        # HINT: try python3 $PWD/client.py read > smaragdine-data.pb
        print(client.read())
    elif args.command in ['smoke_test', 'test', 'smoke-test', 'smoketest']:
        client.start(args.pid)
        sleep(1)
        client.stop()
        print(client.read())


if __name__ == '__main__':
    main()
