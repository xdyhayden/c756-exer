#!/usr/bin/env bash
# Build and run the CI test
set -o errexit
set -o errexit
set -o xtrace
./buildall.sh
docker-compose up
./create-local-tables.sh
