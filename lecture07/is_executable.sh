#!/bin/sh

# Check if each command line argument is executable

EXECUTABLE=""

for arg in $@; do
    if [ -x "$arg" ]; then
	EXECUTABLE="$EXECUTABLE $arg"
    fi
done

echo "The following files are executable:$EXECUTABLE"
