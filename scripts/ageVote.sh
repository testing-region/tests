#! /usr/bin/bash

age=5

## using and operator
#if [ $age -gt 18 -a  $age -lt 60 ]
#then
#	echo "You are legal"
#else
#	echo "You are illegal"
#fi

## using or operator
#if [ $age -gt 19 -o $age -eq 60 ]
#then
#	echo "I don't know about you"
#else
#	echo "Maybe I might know you"
#fi

## Using pipe (symbols)
if [[ $age -gt 19 || $age -eq 60 ]]
then
	echo "What is this?"
else
	echo "Something will happen"
fi
