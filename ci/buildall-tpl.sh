#!/usr/bin/env bash
# Build all necessary services for CI
creg=ZZ-CR-ID
regid=ZZ-REG-ID
ver=v1
./builddb.sh ${creg} ${regid} ${ver}
./builds1.sh ${creg} ${regid} ${ver}
./builds2.sh ${creg} ${regid} ${ver}
./buildci.sh ${creg} ${regid} ${ver}

