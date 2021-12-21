#!/usr/bin/env bash
# Build and run the CI test
# This is intended to be run in a fresh environment,
# such as a GitHub action, where no prior
# images exist.  If you want to test your CI locally,
# use `runci-local.sh` instead.
set -o errexit
set -o nounset

if [[ $# -gt 1 ]]; then
  echo "Usage: ${0} [VERSION]"
  echo "Run the continuous integration tests"
  echo
  echo "  VERSION the version subdirectory of the test code (v1, ...)"
  echo "  default: v1"
  exit 1
elif [[ $# -eq 1 ]]; then
  ver="${1}"
else
  ver=v1
fi

if [[ ! -d ${ver} ]]; then
  echo "'${ver}' is not a subdirectory of the current directory"
  exit 2
fi

set -o xtrace
docker-compose -f ${ver}/compose.yaml up --abort-on-container-exit --exit-code-from test
# Return code from 'up' is the test result
trc=$?
# Shutdown and delete all the containers before returning
docker-compose -f ${ver}/compose.yaml down
exit ${trc}
