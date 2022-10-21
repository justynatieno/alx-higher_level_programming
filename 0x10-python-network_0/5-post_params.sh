#!/bin/bash
#  script that takes in a URL, sends a POST request to the passed URL
curl -sd "email=test@gmai.com&subject=I will always be here for PLD" -X POST "$1"
