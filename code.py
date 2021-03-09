import time
import adafruit_trellism4


trellis = adafruit_trellism4.TrellisM4Express()

time.sleep(0.35)

for y in range (4):
        trellis.pixels[6,y] = (20,20,0)
for x in range (6,1,-1):
        trellis.pixels[x,3] = (20,20,0)
for y in range (3,-1,-1):
        trellis.pixels[2,y] = (20,20,0)

while True:
    pressed = set(trellis.pressed_keys)
    for press in pressed:
        if press:
            print("Pressed:", press)
            x, y = press
            if x<=5 and x>=3 and y<=2:
                trellis.pixels[x,y] = (20,0,0)

    