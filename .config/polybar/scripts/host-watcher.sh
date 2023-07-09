#!/bin/bash

 srv=`ping 10.0.5.3 -c 1 -W 1 \
  | sed '2q;d' \
  | awk 'NF>1{print $NF}'`

 fail=`date '+%a %H:%M:%S'`



 if [[ $srv == ms ]]; then
      echo ""
     :

 else

     echo " "

 fi
