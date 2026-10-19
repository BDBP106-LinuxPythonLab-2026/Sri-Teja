#!/bin/bash

#(i)
awk ' $2<25  {print "people who scored less than 25 in their subjects are " $1} ' info.txt

#(ii)
awk ' $3=="Physics" {print "Student whose physics marks are given is " $1}' info.txt

#(iii)
awk '{print $1"," $2 "," $3}' info.txt > data.csv
