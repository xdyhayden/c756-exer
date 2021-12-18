#!/usr/bin/env bash
# Build and run the CI test
# This is intended to be run in a fresh environment,
# such as a GitHub action, where no prior
# images exist.  If you want to test your CI locally,
# use `runci-local.sh` instead.
set -o errexit
set -o nounset
set -o xtrace
docker-compose up --exit-code-from test
trc=$?
docker-compose down
exit ${trc}
