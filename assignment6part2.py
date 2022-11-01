#=====================
# STIMULUS EXERCISES
#=====================

# Import
from psychopy import gui, visual, monitors, event
import os
import numpy
import time


# access images
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
# set up monitor and window
mon = monitors.Monitor('myMonitor', width=24.5, distance=60)
mon.setSizePix([1920,1080])
win = visual.Window(monitor=mon, fullscr=True)
# image set up
my_image = visual.ImageStim(win)
# adding the properties units="pix" and size=(400) distorts the image
# to rezise image, instead you can resize during trial for loop
# set # of trials
nTrials = 4
# making a list of the names of the stimuli
num = []
for i in range(10): 
    num.append(i+1)
pics = ["face" + (str(i).zfill(2)) + ".jpg" for i in num]
numpy.random.shuffle(pics)

# set up fixation cross
cross = "+"
fx_cross = visual.TextStim(win, text=cross)

print(win.size)
# list the 4 valid locations. We are using height units for simplicity
locs = [(0.6,0.45), (-0.6,0.45), (-0.6,-0.45), (0.6,-0.45)]
# 0.8 and 0.5 are the very edges of the height and width (with my aspect ratio), but we give it some buffer because the images are drawn from their center

# trials
for trial in range(nTrials):
    #-draw fixation
    fx_cross.draw()
    #-flip window
    win.flip()
    #-wait time (stimulus duration)
    time.sleep(1)
    
    # get image ready
    my_image.image = os.path.join(image_dir,pics[trial])
    # reset image size to default so it doesn't just keep growing
    my_image.size = None
    # have to resize in for loop so that it is image specific, prevent distortion
    # this multiplies the width and height values of each image, retaining aspect ratio
    my_image.size *= (1.1,1.1)
    # set position by iterating through previously set list of positions
    my_image.pos = locs[trial]
    
    # draw image
    my_image.draw()
    win.flip()
    event.waitKeys()
    
# close window
win.close()

