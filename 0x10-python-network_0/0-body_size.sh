#!/bin/bash
# taes url, send request to the url and display size of esponse body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2 
