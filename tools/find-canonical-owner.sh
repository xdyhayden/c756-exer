#!/usr/bin/env bash

#
# This derives the canonical owner of a repo within the organization
# for the purpose of generating the hash code for Assignment 1-3
#
# This is necessary as a GitHub Education student's repo resides within the same organization as the instructor
#

reponame=${1}
repoowner=${2}

# strip out the owning organization to reduce the required update for when the repo/assignment moves
barename=`echo ${reponame} | cut -d \/ -f 2`

if [ ${barename} = "c756-exer" ]; then
  echo "canonical-owner="${repoowner}
else
  # the fragment below will need to be adjusted when 1) the template repo moves to a new organization or 
  #  2) the assignment is renamed.
  echo "caonical-owner="${reponame} | sed -e "s/scp756-221\/assignments-//" 
fi
