#!/bin/bash

# Variables
URL="localhost"
PORT=2375
METHOD="POST"
RESOURCE="containers"
CONTAINER_NAME="dcf_dhcp"
ACTION="kill"

# BODY
RESULT=$(curl -i -X ${METHOD} ${URL}:${PORT}/${RESOURCE}/${CONTAINER_NAME}/${ACTION})
echo ${RESULT}
