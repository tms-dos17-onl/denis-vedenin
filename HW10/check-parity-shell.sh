#!/bin/sh

num=$1

if [ -z "$num" ]; then
	echo "Аргумент не является числом"
else
	if [ $(("$num" % 2)) -eq 0 ]; then
		echo "чётное"
	else
		echo "нечётное"
	fi
fi
