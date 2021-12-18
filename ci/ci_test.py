"""
Integration test of the CMPT 756 sample applicaton.

Result of test in program return code:
0: Test succeeded
1: Test failed
"""

# Standard library modules
import argparse
import os
import sys

# Installed packages

# Local modules
import create_tables
import music

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
        help="DNS name or IP address of user service."
        )
    argp.add_argument(
        'user_port',
        type=int,
        help="Port number of user service."
        )
    argp.add_argument(
        'music_address',
        help="DNS name or IP address of music service."
        )
    argp.add_argument(
        'music_port',
        type=int,
        help="Port number of music service."
        )
    argp.add_argument(
        'table_suffix',
        help="Suffix to add to table names (not including leading "
             "'-').  If suffix is 'scp756-2022', the music table "
             "will be 'Music-scp756-2022'."
    )
    args = argp.parse_args()
    args.user_url = "http://{}:{}/api/v1/user/".format(
        args.user_address, args.user_port)
    args.music_url = "http://{}:{}/api/v1/music/".format(
        args.music_address, args.music_port)
    return args


def get_env_vars(args):
    # These are required to be present
    args.dynamodb_region = os.getenv('AWS_REGION')
    args.access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    args.secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    args.loader_token = os.getenv('SVC_LOADER_TOKEN')
    args.dynamodb_url = os.getenv('DYNAMODB_URL')


def setup(args):
    get_env_vars(args)
    create_tables.create_tables(
        args.dynamodb_url,
        args.dynamodb_region,
        args.access_key_id,
        args.secret_access_key,
        'Music-' + args.table_suffix,
        'User-' + args.table_suffix
    )


def run_test(args):
    mserv = music.Music(args.music_url, DUMMY_AUTH)
    artist, song = ('Mary Chapin Carpenter', 'John Doe No. 24')
    trc, m_id = mserv.create(artist, song)
    if trc != 200:
        sys.exit(1)
    trc, ra, rs = mserv.read(m_id)
    if trc == 200:
        if artist != ra or song != rs:
            # Fake HTTP code to indicate error
            trc = 601
        mserv.delete(m_id)
    return trc


if __name__ == '__main__':
    args = parse_args()
    setup(args)
    trc = run_test(args)
    if trc != 200:
        sys.exit(1)
