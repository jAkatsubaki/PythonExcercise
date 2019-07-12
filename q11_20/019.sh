#!/bin/bash

sort ./hightemp.txt --key=3,3 --numeric-sort --reverse > hightemp_sort_temp_reverse.txt
