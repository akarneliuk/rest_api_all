#!/bin/bash

# Variables
URL=localhost
PORT=2375
METHOD=GET
RESOURCE=images/json

# BODY
RESULT=$(curl -X ${METHOD} ${URL}:${PORT}/${RESOURCE})
echo ${RESULT}
