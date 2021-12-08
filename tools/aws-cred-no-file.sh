#!/usr/bin/env bash
# Set AWS configuration and CMPT 756 token file directly 
# with no intervening file.
# User must have at most one access key.

# For bash tips, see https://devhints.io/bash 

# Strict mode (because this is security-sensitive)
set -o nounset
set -o errexit
set -o pipefail
IFS=$'\n\t'

usage() {
  cat <<EOF
Usage: ${0}
Configure AWS and the CMPT 756 software to use a new access key.

The current user cannot already have two AWS access keys (whether
active or inactive).
EOF
}

if [[ $# -ne 0 ]]
then
  usage
  exit 1
fi

# Count number of keys (active and inactive) for this user
key_count=$(aws iam list-access-keys --output json | jq '.AccessKeyMetadata | length') || true

if [[ $? -ne 0 ]]
then
  cat <<EOF
The query of your key count failed, perhaps due to an invalid key.
Use the AWS Console to set up a valid, active key.
Instead of using this script, download the key as a CSV and use
"tools/aws-cred.sh" to set your key.
EOF
  exit 1
elif [[ ${key_count} -ge 2 ]]
then
  cat <<EOF
You have two keys already.  One must be deleted before running
this script.
EOF
  exit 2
fi

key_id_value=$(aws iam create-access-key --output json | jq '.AccessKey | .AccessKeyId, .SecretAccessKey')

# Next line just for testing
#key_id_value=$(cat test.json | jq '.AccessKey | .AccessKeyId, .SecretAccessKey')

# key_id_value has format "20-char-key-id" "40-char-key-value"
aws_id=${key_id_value:1:20}
aws_key=${key_id_value:24:40}

# Configure the AWS command-line tools
aws configure set aws_access_key_id     ${aws_id}
aws configure set aws_secret_access_key ${aws_key}

# Configure the CMPT 756 files
# The official AWS docs (https://docs.aws.amazon.com/IAM/latest/APIReference/API_AccessKey.html) state that Access Key IDs are pure alphanumeric.
# They do not restrict the Secret Access Key in any way but various sites on the Web suggest that it is only alphanumeric+slash+plus
# So it should be delimitable by '|'
sed -e "s|ZZ-AWS-ACCESS-KEY-ID=.*|ZZ-AWS-ACCESS-KEY-ID=${aws_id}|"           \
    -e "s|ZZ-AWS-SECRET-ACCESS-KEY=.*|ZZ-AWS-SECRET-ACCESS-KEY=${aws_key}|"  \
  -i cluster/tpl-vars.txt
