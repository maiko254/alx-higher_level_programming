#!/bin/bash
# sends a GET request with a request header variable to a URL and displays the response
curl -s -H "X-School-User-Id: 98" "$1"
