"""
Integration test of the CMPT 756 sample applicaton.

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
DUMMY_AUTH = 'Bearer A'


def parse_args():
    argp = argparse.ArgumentParser(
        'ci_test',
        description='Integration test of CMPT 756 sample application'
        )
    argp.add_argument(
        'user_address',
        help="DNS name or IP address of user service"
        )
    argp.add_argument(
        'user_port',
        type=int,
        help="Port number of user service"
        )
    argp.add_argument(
        'music_address',
        help="DNS name or IP address of music service"
        )
    argp.add_argument(
        'music_port',
        type=int,
        help="Port number of music service"
        )
    args = argp.parse_args()
    args.user_url = "http://{}:{}/api/v1/user/".format(
        args.user_address, args.user_port)
    args.music_url = "http://{}:{}/api/v1/music/".format(
        args.music_address, args.music_port)
    return args


def music_create(args, artist, song):
    r = requests.post(
        args.music_url,
        json={'Artist': artist,
              'SongTitle': song},
        headers={'Authorization': DUMMY_AUTH}
        )
    return r.status_code, r.json()['music_id']


def music_read(args, m_id):
    r = requests.get(
        args.music_url + m_id,
        headers={'Authorization': DUMMY_AUTH}
        )
    return r.status_code


def music_delete(args, m_id):
    _ = requests.delete(
        args.music_url + m_id,
        headers={'Authorization': DUMMY_AUTH}
        )
    # Music delete does not return a status code
    return 200


if __name__ == '__main__':
    args = parse_args()
    trc, m_id = music_create(
        args, 'Mary Chapin Carpenter', 'John Doe No. 24')
    if trc != 200:
        sys.exit(1)
    trc = music_read(args, m_id)
    music_delete(args, m_id)
    if trc != 200:
        sys.exit(1)
