import numpy as np
import scipy.misc as smp
from PIL.Image import fromarray

from hedge import hedge_anim_move
#test

def calc_pixel(bildnr, x, y):
    global spaltenProBild
    global Bilderanzahl
    pre_offset = bildnr * spaltenProBild
    idx = y+x*spaltenProBild
    post_offset = (Bilderanzahl - 1 - spaltenProBild) * spaltenProBild
    return (pre_offset + idx + post_offset) 

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros( (24, 24, 3), dtype=np.uint8 )


#data[20, 20] = [254,0,0]       # Makes the middle pixel red
#data[10, 10] = [0,0,255]       # Makes the next pixel blue

spaltenProBild = 24
Bilderanzahl = 6


print("size   : ", 24+24*spaltenProBild*Bilderanzahl)
print("arrsize: ", len(hedge_anim_move) )

bildnr = 0
for y in range(0, 23):
    for x in range(0, 23):
        pre_offset = bildnr * spaltenProBild
        idx = y+x*spaltenProBild
        post_offset = (Bilderanzahl - 1 - spaltenProBild) * spaltenProBild
        i = calc_pixel(bildnr, x, y)
        pix2 = hedge_anim_move[pre_offset + idx + post_offset]
        pix = hedge_anim_move[i]
        if (pix != pix2):
            print("ERRROROROROROR: ", pix, " != " , pix2)
        R = pix & 0xff
        G = (pix >> 8) & 0xff
        B = (pix >> 16) & 0xff

        data[x,y] = (R,G,B)
img = fromarray(np.array(data))
img.show()  

bildnr = 1
for y in range(0, 23):
    for x in range(0, 23):
        pix = hedge_anim_move[y+x*spaltenProBild*Bilderanzahl]
        # Farben konvertieren (von 5+6+5 Bit in uint32_t nach 8+8+8 Bit)
        R = pix & 0xff
        G = (pix >> 8) & 0xff
        B = (pix >> 16) & 0xff
        data[x,y] = (R,G,B)

img = fromarray(np.array(data))
img.show()  

bildnr = 2

for y in range(0, 23):
    for x in range(0, 23):
        pix = hedge_anim_move[y+x*spaltenProBild*Bilderanzahl]
        # Farben konvertieren (von 5+6+5 Bit in uint32_t nach 8+8+8 Bit)
        R = pix & 0xff
        G = (pix >> 8) & 0xff
        B = (pix >> 16) & 0xff
        data[x,y] = (R,G,B)

img = fromarray(np.array(data))
img.show()  




