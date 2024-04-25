#!/bin/bash
# a bash script that takes an url and send a get request                                                 
if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; 
then 
curl -sL "$1"; 
fi