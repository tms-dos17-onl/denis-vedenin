#!/bin/bash

num=$1
exem=$([[ $num =~ ^[0-9]+$ ]])
case $num in
$exam)
        echo "Аргумент не является числом"
        ;;
*)
        [[ $(expr "$1" % 2) -eq 0 ]] && echo "чётное" || echo "нечётное"
        ;;
esac
