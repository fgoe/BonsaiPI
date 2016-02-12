/usr/bin/rrdtool graph /var/www/html/bonsai/graphs/humi.png -a PNG -b 1024 --slope-mode --start -86400 -A \
-c MGRID#380000 -t "Volumetric Moisture Content - Tag" --vertical-label "Erdfeuchte in Prozent" -w 500 -h 250 \
DEF:g1=/var/www/html/bonsai/rrds/PIdata.rrd:VMC:AVERAGE \
DEF:g1min=/var/www/html/bonsai/rrds/PIdata.rrd:VMC:MIN \
DEF:g1max=/var/www/html/bonsai/rrds/PIdata.rrd:VMC:MAX \
VDEF:g1a=g1,LAST \
VDEF:g1mina=g1min,MINIMUM \
VDEF:g1maxa=g1max,MAXIMUM \
VDEF:g1durch=g1,AVERAGE \
AREA:g1#66FF33 \
LINE2:g1#336633:"Erdfeuchte\n" \
GPRINT:g1a:"Aktuell\:  %5.2lf Prozent" \
GPRINT:g1durch:"Durchschnitt\: %5.2lf Prozent" \
GPRINT:g1mina:"Tiefste\: %5.2lf Prozent" \
GPRINT:g1maxa:"Hoechste\: %5.2lf Prozent" > /dev/null

/usr/bin/rrdtool graph /var/www/html/bonsai/graphs/humi_week.png -a PNG -b 1024 --slope-mode --start -604800 -A \
-c MGRID#380000 -t "Volumetric Moisture Content - Week" --vertical-label "Erdfeuchte in Prozent" -w 500 -h 250 \
DEF:g1=/var/www/html/bonsai/rrds/PIdata.rrd:VMC:AVERAGE \
DEF:g1min=/var/www/html/bonsai/rrds/PIdata.rrd:VMC:MIN \
DEF:g1max=/var/www/html/bonsai/rrds/PIdata.rrd:VMC:MAX \
VDEF:g1a=g1,LAST \
VDEF:g1mina=g1min,MINIMUM \
VDEF:g1maxa=g1max,MAXIMUM \
VDEF:g1durch=g1,AVERAGE \
AREA:g1#66ff33 \
LINE2:g1#336633:"Erdfeuchte\n" \
GPRINT:g1a:"Aktuell\:  %5.2lf Prozent" \
GPRINT:g1durch:"Durchschnitt\: %5.2lf Prozent" \
GPRINT:g1mina:"Tiefste\: %5.2lf Prozent" \
GPRINT:g1maxa:"Hoechste\: %5.2lf Prozent" > /dev/null
