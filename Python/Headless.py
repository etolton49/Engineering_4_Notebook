Fix
# Headless
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)


# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

#Creating instance with LSM
lsm303 = Adafruit_LSM303.LSM303()

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
x = 2
top = 2
padding = 12

font = ImageFont.load_default()

dot_arr = []
dot_max = 50
def map_range(a, b, s):
    (a1, a2), (b1, b2) = a, b
    return b1 + ((s -a1) * (b2 - b1) / (a2 - a1))

while True:
    #Clearing OLED with blank rectangle
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    #Drawing graph
    draw.line((padding, height-padding, padding, -height+padding), fill=255)
    draw.line((padding, height-padding, padding+width, height-padding), fill=255)
    

    accel, mag = lsm303.read()
    accel_x = accel[0]

    if len(dot_arr) <= 115:
        dot_arr.append(accel_x)
    else:
        del dot_arr[0]
        dot_arr.append(accel_x)
    x_pos = 15
    #print(dot_arr)
    for i in range(1,len(dot_arr)):
        y_pos = map_range((520, -520), (0 , height - padding), dot_arr[i])
        last_y_pos = map_range((520, -520), (0 , height - padding), dot_arr[i-1])
        y_pos = round(y_pos)
        #print(str(y_pos))
        draw.point((x_pos, y_pos), fill=255)
        draw.line((x_pos,y_pos,x_pos-1,last_y_pos), fill=255)
        
        x_pos += 1
    
    disp.image(image)
    disp.display()
    time.sleep(.05)
   


