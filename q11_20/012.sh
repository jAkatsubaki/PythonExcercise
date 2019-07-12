#!/bin/bash

cat ./hightemp.txt > hightemp.txt.bak
sed -i -e 's/\t/ /g' ./hightemp.txt
