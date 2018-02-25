import piconzero as pz, time
pz.init()
#pz.setOutputConfig(0, 2)
pz.setInputConfig(0, 1)
rest = 0.5
try:
    while True:      
        angle = pz.readInput(0)
        print('angle: ', angle)
        time.sleep(rest)
except KeyboardInterrupt:
    print
    pz.cleanup()