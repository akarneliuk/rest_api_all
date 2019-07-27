#!/bin/bash

# Variables
URL="localhost"
PORT=32768
TOKEN=0123456789abcdef0123456789abcdef01234567
METHOD="POST"
RESOURCE="api/dcim/devices/"

# BODY
RESULT=$(curl -i -X ${METHOD} ${URL}:${PORT}/${RESOURCE} \
    --header "Authorization: Token ${TOKEN}" \
    --header "Content-Type: application/json" \
    --data '{"name": "de-test-spine-333", "device_type": 3, "device_role": 3, "site": 1, "status": 2}')
echo ${RESULT}
