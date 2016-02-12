#!/bin/bash

# Path to executables
rrdtool=/usr/bin/rrdtool
sleep=/bin/sleep

# Path to RRD File
rrddb=/var/www/html/bonsai/rrds/PIdata.rrd

# Sleep for 10s to wait temporary file to be created
sleep 10

# Create Value file in /tmp
file="/tmp/VWCvalue"
VWCvalue=$(cat "$file")
echo $VWCvalue

# Update rrd database
$rrdtool update $rrddb N:$VWCvalue
