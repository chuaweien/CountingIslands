#!/usr/bin/env bash

# get filepath passed as an argument
filepath=$1 

# check if filepath was passed as an argument,
# otherwise exit with error 1
if [ -z "$filepath" ]; then
    echo "Please provide a filepath as an argument."
    exit 1
fi

# check if file exists at the filepath,
# otherwise exit with error 1
if [ ! -f "$filepath" ]; then
    echo "File does not exist at the provided filepath."
    exit 1
fi

# run python script, passing the filepath as an argument
python src/run.py "$filepath"

# check if the script execution was successful,
# otherwise exit with error 1
if [ $? -eq 0 ]; then
    echo "Island Counting script execution was successful."
else
    echo "Island Counting script execution failed."
    exit 1
fi