#!/bin/bash

# Check if the number of arguments provided is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided as an argument
URL=$1

# Use curl to send a GET request to the URL and capture the response body size
# -s option is used to suppress curl's progress meter and other unnecessary output
# -o /dev/null option is used to redirect the response body to /dev/null, as we are only interested in the size
# -w "%{size_download}" option is used to print the size of the downloaded data
SIZE=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

# Print the size of the response body in bytes
echo "$SIZE"
