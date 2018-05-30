#import sys
import time
#import difflib
import pigpio
import re

RX=18

def parse_GPS_msg(msg):
    temp = msg[re.search("GPGGA", msg).span()[0]:
        re.search("GPGSA", msg).span()[0]].split(',')
    UTC_Time = temp[1]
    lat = round((int(temp[2][0:2]) + int(temp[2][2:4])/60 + \
        float(temp[2][4:len(temp[2])])) * (1 if temp[3] == 'N' else -1), 4)
    long = round((int(temp[4][0:3]) + int(temp[4][3:5])/60 + \
        float(temp[4][5:len(temp[4])])) * (1 if temp[5] == 'E' else -1), 4)
    GPSQI = temp[6]
    sat_count = temp[7]
    alt = temp[9]
    return {'UTC_Time': float(UTC_Time), 'lat': float(lat), 'long': float(long), 
            'alt': float(alt), 'sat_count': int(sat_count)}

try:
        pi = pigpio.pi()
        pi.set_mode(RX, pigpio.INPUT)
        pi.bb_serial_read_open(RX, 9600, 8)
        while 1:
                (count, data) = pi.bb_serial_read(RX)
                if count:
                        print(parse_GPS_msg(str(data)))
                time.sleep(1)

except:
        pi.bb_serial_read_close(RX)
        pi.stop()
        
        
   
