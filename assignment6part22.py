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
my_image = visual.ImageStim(win, units = "pix")
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
# list the 4 valid locations. We are using pixel units for simplicity
locs = [(-600,-300), (-600,300), (600,-300), (600,300)]
# we give the positions some buffer because the images are drawn from their center
# shuffle this too because we love randomizaTION
numpy.random.shuffle(locs)

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
    # reset image size to default so it doesn't stay the same ratio
    my_image.size = None
    # get current image size
    print(my_image.size)
    # we want max size to be 400px. so use the biggest dimension of the image to find the scaling ratio
    rem = 400.0/max(my_image.size)
    # set image size // round the image dimensions multiplied by scaling factor and treat it as an integer
    my_image.size = numpy.around(my_image.size * rem).astype(int)
    # set position by iterating through previously set list of positions
    my_image.pos = locs[trial]
    
    # draw image
    my_image.draw()
    win.flip()
    
    
    event.waitKeys()
    
# close window
win.close()

