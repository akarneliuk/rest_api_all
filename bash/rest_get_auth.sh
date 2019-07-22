#!/bin/bash

# Variables
URL=localhost
PORT=32768
TOKEN=0123456789abcdef0123456789abcdef01234567
METHOD=GET
RESOURCE=api/dcim/devices/

# BODY
RESULT=$(curl -X ${METHOD} ${URL}:${PORT}/${RESOURCE} --header "Authorization: Token ${TOKEN}")
echo ${RESULT}
