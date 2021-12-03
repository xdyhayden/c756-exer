#!/usr/bin/env bash
# Run the service with the code for A1
set -o nounset
set -o errexit
make VER=v0.25 HWD=${HWD} run-s2
