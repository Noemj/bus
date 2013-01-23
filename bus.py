from xml.dom.minidom import parse,parseString
import datetime
import urllib2
import sys

if len(sys.argv)>1:
    time = sys.argv[1]
else:
    now = datetime.datetime.now()
    time = str(now.hour) + str(now.minute)

xml = urllib2.urlopen('http://api.reittiopas.fi/public-ytv/fi/api/?a=2556309,6679691&b=2553603,6677524&time=' + time + '&timemode=1&user=username&pass=password')
timetable = parse(xml)
routes = timetable.getElementsByTagName('ROUTE')
for route in routes:
    lines = route.getElementsByTagName('LINE')
    for line in lines:   
        stops = line.getElementsByTagName('STOP')

        for stop in stops:
            name = stop.getElementsByTagName('NAME')
            val = map(lambda p: p.getAttribute('val'),name)
            if 'A.I. Virtasen aukio' in val:
                arrival = stop.getElementsByTagName('ARRIVAL')
                time = map(lambda p: p.getAttribute('time'),arrival)
                print 'Next 506 leaving from Kumpula at: ' + str(time).split('\'')[1]
                sys.exit(0)

print 'Vika meni jo.. '