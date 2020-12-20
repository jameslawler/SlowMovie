#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, time
from PIL import Image

import arguments.getArgs
import state

# Ensure this is the correct import for your particular screen 
from waveshare_epd import epd7in5_V2 as epd_driver

# Ensure this is the correct path to your video folder 
imagesDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Images/')

# Get argument inputs and set constants
args = arguments.getArgs()

frameDelay = float(args.delay)

if args.start:
  currentPosition = float(args.start)
else:
  currentPosition = state.getCurrentPosition()

epd = epd_driver.EPD()

# Initialise and clear the screen 
epd.init()
epd.Clear()    

while 1: 
  # Open frame image in PIL if found (otherwise exit program)
  imageFilePath = imagesDirectory + str(currentPosition).zfill(4) + ".png"
  if not os.path.exists(imageFilePath):
    print("Image not found (" + imageFilePath + "). Exiting Program")
    epd.Clear()
    epd.sleep()
    epd7in5.epdconfig.module_exit()
    exit()

  pil_im = Image.open(imageFilePath)
  
  # Dither the image into a 1 bit bitmap (Just zeros and ones)
  pil_im = pil_im.convert(mode='1',dither=Image.FLOYDSTEINBERG)

  # Display the image 
  epd.display(epd.getbuffer(pil_im))

  # Store current position in case program restarts
  state.saveCurrentPosition(currentPosition)

  # Wait for delay until next frame is shown
  epd.sleep()
  time.sleep(frameDelay)
  epd.init()

epd.Clear()
epd.sleep()
epd7in5.epdconfig.module_exit()

exit()
