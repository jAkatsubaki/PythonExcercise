#!/bin/sh

cut -f 1 -d ' ' ./hightemp.txt | sort | uniq --count | sort --reverse
