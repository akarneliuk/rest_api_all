#!/bin/bash

# Variables
URL=localhost
PORT=32768
METHOD=GET
RESOURCE=api/dcim/devices/
TOKEN=0123456789abcdef0123456789abcdef01234567

# BODY
RESULT=$(curl -X ${METHOD} ${URL}:${PORT}/${RESOURCE} --header "Authorization: Token ${TOKEN}")
echo ${RESULT}
