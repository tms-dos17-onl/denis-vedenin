#!/bin/bash

num=$1

case $num in
"$([[ $num =~ ^[0-9]+$ ]])")
	echo "Аргумент не является числом"
	;;
*)
	[[ $(("$1" % 2)) -eq 0 ]] && echo "чётное" || echo "нечётное"
	;;
esac
