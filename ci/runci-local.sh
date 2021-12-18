#!/usr/bin/env bash
# Run the CI tests locally.
# You will likely want to modify this or create a variant
# to meet your needs.
# This version is simple and correct but potentially slow:
# It forces a rebuild of every image on every run.  This
# guarantees that the latest versions are always used,
# at the expense of potentially unncessary rebuilds.
# You may want to be more selective in your rebuilds to
# speed up the process.
set -o nounset
set -o errexit
./clear-ci-images.sh
./runci.sh

