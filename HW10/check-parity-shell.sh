#!/bin/sh

#ПРоверка на четность
if [ $(expr "$1" % 2) -eq 0 ]; then
    echo "чётное"
elif [ $(expr "$1" % 2) -ne 0 ]; then
    echo "нечётное"
else
    echo "Аргумент не является числом"
    exit 1
fi
