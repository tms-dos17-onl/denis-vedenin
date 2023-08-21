#!/usr/bin/env bash

FILENAME=$(ls)
# Check if the file is empty
#if [ ! -s "${FILENAME}" ]; then
#    echo "$FILENAME" "File is empty"
#fi

if [ -f "${FILENAME}" ]; then
        if [ -s "${FILENAME}" ]; then
            echo "File ${FILENAME} существует и не пуст"
        else
            echo "File ${FILENAME} существует но пуст"
        fi
else
        echo "File ${FILENAME} не существует"
fi
