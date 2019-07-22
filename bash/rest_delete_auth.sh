#!/bin/bash

# Variables
URL="localhost"
PORT=32768
TOKEN=0123456789abcdef0123456789abcdef01234567
METHOD="DELETE"
RESOURCE="api/dcim/devices/"
ID="18/"

# BODY
RESULT=$(curl -i -X ${METHOD} ${URL}:${PORT}/${RESOURCE}${ID} \
    --header "Authorization: Token ${TOKEN}")
echo ${RESULT}
