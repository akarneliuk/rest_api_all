#!/bin/bash

# Variables
URL="localhost"
PORT=32768
TOKEN=0123456789abcdef0123456789abcdef01234567
METHOD="PATCH"
RESOURCE="api/dcim/devices"
ID="30"

# BODY
RESULT=$(curl -i -X ${METHOD} ${URL}:${PORT}/${RESOURCE}/${ID}/ \
    --header "Authorization: Token ${TOKEN}" \
    --header "Content-Type: application/json" \
    --data '{"device_type": 3, "device_role": 3, "site": 1, "status": 3}')
echo ${RESULT}
