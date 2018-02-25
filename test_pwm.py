# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 07:10:18 2018

@author: ccgar
"""

import piconzero as pz, time
pz.init()
pz.setOutputConfig(0, 1)
rest = 5
try:
    while True:
        for i in range(0,101,5):
            print str(i) + ' degrees'
            pz.setOutput(0, i) 
            time.sleep(rest)
            pz.setOutput(0, 0) 
            time.sleep(rest)
except KeyboardInterrupt:
    print
    pz.cleanup( )