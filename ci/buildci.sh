# Build the ci_test application
set -o nounset
set -o errexit
if [[ $# -ne 3 ]]; then
  echo "Usage: ${0} CREG REGID VER"
  echo "Build the CI test"
  echo "  CREG Container registry"
  echo "  REGID Userid for container registry"
  echo "  VER Version"
  exit 1
fi
set -o xtrace
docker build -t ${1}/${2}/ci_test:${3} .

