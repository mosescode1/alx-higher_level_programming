#!/bin/bash
# displaying the header size in bytes
curl -s -w "%{size_download}" -o /dev/null $1
