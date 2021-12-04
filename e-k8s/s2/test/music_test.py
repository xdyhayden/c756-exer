"""
Simple test that calls `test` then `shutdown`.

Result of test in program return code:
0: Test succeeded
1: Test failed
"""

# Standard library modules
import argparse
import sys

# Installed packages
import requests

# The services check only that we pass an authorization,
# not whether it's valid
DEFAULT_AUTH = 'Bearer A'


def parse_args():
    argp = argparse.ArgumentParser(
        'music_test',
        description='Simple test of music service'
        )
    argp.add_argument(
        'name',
        help="DNS name or IP address of music server"
        )
    argp.add_argument(
        'port',
        type=int,
        help="Port number of music server"
        )
    return argp.parse_args()


def get_url(name, port):
    return "http://{}:{}/api/v1/music/".format(name, port)


def test(args):
    url = get_url(args.name, args.port)
    r = requests.get(
        url+'test',
        headers={'Authorization': DEFAULT_AUTH}
        )
    if r.status_code != 200:
        sys.exit(1)


def shutdown(args):
    url = get_url(args.name, args.port)
    r = requests.get(
        url+'shutdown',
        headers={'Authorization': DEFAULT_AUTH}
        )
    if r.status_code != 200:
        sys.exit(1)


if __name__ == '__main__':
    args = parse_args()
    test(args)
    shutdown(args)
    sys.exit(0)
