#!/bin/bash

cut --fields=1 -d ' ' ./hightemp.txt | sort | uniq > hightemp_sort.txt
