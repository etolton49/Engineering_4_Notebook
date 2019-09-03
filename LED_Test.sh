#!/bin/bash

gpio mode 29 out
gpio mode 28 out

for i in {1..10}
do 
	gpio write 29 1
	gpio write 28 1
	sleep .3
	gpio write 29 0
	gpio write 28 0
	sleep .3
done
