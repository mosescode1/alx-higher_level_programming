#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -si $1 | grep -i allow | sed 's/Allow: //i
