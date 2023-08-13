#!/bin/bash
chet=$([ $(expr "$1" % 2) -eq 0 ])
nechet=$([ $(expr "$1" % 2) -ne 0 ])

case $1 in
$chet ) echo "чётное" ;;
$nechet ) echo "нечётное" ;;
* ) echo "Аргумент не является числом" ;;
esac
