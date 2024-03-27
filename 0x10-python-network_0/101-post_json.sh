#!/bin/bash
# This script sends a JSON POST request to a URL and displays the response body.
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
