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
    --data '{"status": 1, "serial": "SN:00:11:22:33:44", "rack": 3, "tags": ["pimped"]}')
echo ${RESULT}
