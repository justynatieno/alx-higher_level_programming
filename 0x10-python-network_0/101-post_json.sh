#!/bin/bash
# sends a JSON post request and displays the body of the response
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
