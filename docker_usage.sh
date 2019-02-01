#!/bin/sh

while true
do

 docker stats --no-stream |grep 8ca71ff08cc2 > docker_usage.txt
 python3 docker_detect.py
 sleep 10

done
