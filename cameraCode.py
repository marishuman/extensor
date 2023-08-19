from pyb import UART, ADC

 
adc = ADC("P6") # Must always be "P6".

 
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster (160x120 max on OpenMV-M7)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()
uart = UART(3, 9600)

 
compDistance = adc.read()
actDistance = -0.0031*compDistance + 16.662
print(actDistance)

 
while(True):
    clock.tick()
    img = sensor.snapshot()

 
    # `threshold` below should be set to a high enough value to filter out noise
    # rectangles detected in the image which have low edge magnitudes. Rectangles
    # have larger edge magnitudes the larger and more contrasty they are...
    

 
    for r in img.find_rects(threshold = 9000):
        img.draw_rectangle(r.rect(), color = (255, 0, 0))
        for p in r.corners(): img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
        compDistance = adc.read()
        actDistance = -0.0031*compDistance + 16.662
        print("Distance:", end = " ") 
        print(actDistance)
        if actDistance <= 8:
            A = 0.0057*actDistance+0.0112
            B = -0.0444*actDistance+0.8225
            x = A*r[2]-B
            #x = -5.4416+0.3665*10+0.0908*r[2] matlab equation test
            # print(r[2])
            # print(x)
            y = '%.4f'%(x)
            print(y)
            uart.write(str(y) + "\n")
            #time.sleep(1)
            #print(r)

 

 
    # print("FPS %f" % clock.fps())
