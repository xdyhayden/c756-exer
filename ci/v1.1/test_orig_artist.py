"""
Test the *_original_artist routines.

These tests are invoked by running `pytest` with the
appropriate options and environment variables, as
defined in `conftest.py`.
"""

# Standard libraries

# Installed packages
import pytest

# Local modules
import music


@pytest.fixture
def mserv(request, music_url, auth):
    return music.Music(music_url, auth)


@pytest.fixture
def m_id(request, mserv, song):
    trc, m_id = mserv.create(song[0], song[1])
    assert trc == 200
    yield m_id
    # CLeanup called after the test completes
    mserv.delete(m_id)


@pytest.fixture
def song(request):
    # Recorded 1956
    return ('Elvis Presley', 'Hound Dog')


def test_orig_artist(mserv, m_id, song):
    # Original recording, 1952
    orig_artist = 'Big Mama Thornton'
    trc = mserv.write_orig_artist(m_id, orig_artist)
    assert trc == 200
    trc, oa = mserv.read_orig_artist(m_id)
    assert trc == 200 and oa == orig_artist
