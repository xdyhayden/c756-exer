#!/usr/bin/env bash
# Remove all images created in a CI run
docker image rm ci_cmpt756db:latest ci_cmpt756s1:latest ci_cmpt756s2:latest ci_test:latest
