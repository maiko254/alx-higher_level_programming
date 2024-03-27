#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -s -I -L -X "OPTIONS" "$1" | grep -i "^Allow:" | sed 's/^Allow: //i'
