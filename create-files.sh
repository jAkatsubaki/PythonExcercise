#!/usr/bin/bash
k=1
kk=0
dir=""
while [ $k -lt 100 ]
do
  kk=$((k+9))
  dir="${k}-${kk}"
  mkdir $dir
  echo "save to ${dir}"
  if [ $k -lt 10 ]; then
    m=1
    while [ $m -lt 9 ]
    do
      echo "" >  $dir/"00${m}".py
      #echo $dir/"00${m}".py
      m=$((m+1))
    done
    echo "" > $dir/"010".py
    #echo $dir/"010".py
  else
    m=$k
    mm=$((k+10))
    while [ $m -lt $mm ]
    do
      echo "" > $dir/"0${m}".py
      #echo $dir/"0${m}".py
      m=$((m+1))
    done
  fi
  k=$((k+10))
done
mv "91-100"/0100.py 100.py
#echo "91-100"/100.py
