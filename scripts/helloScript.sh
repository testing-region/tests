#! /usr/bin/bash

## Print to screen
#echo 'Hello bash script' > file.txt

## Replace text data
#cat > file.txt

## Append to text data 
#cat >> file.txt

## multi-line comments
: '
This is a test
This is a test
/usr/bin/bash
/usr/bin/bash
'
# echo 'Hello World'
: '
cat << some_variable
This is a here doc delimiter
some_variable '


## Conditional statements

### If statement
: '
count=10

if [ $count -lt 10 ]
then
	echo "condition is true"
else
	echo "condition is false"
fi '

### To use normal signs, use '(())'
count=10

if (( count > 10 ))
then
	echo "True"
elif (( count == 10 ))
then
	echo "Count is 10"
else
	echo "False"
fi


