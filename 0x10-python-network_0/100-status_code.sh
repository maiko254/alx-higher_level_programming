#!/bin/bash
# script that displays only the status code of a response to a URL request
curl -s -o /dev/null -w "%{http_code}" "$1"
