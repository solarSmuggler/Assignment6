# IMPORT
from psychopy import gui, visual, monitors, event
import os
import numpy
import time
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
# directory stuff
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
# set up monitor and window
mon = monitors.Monitor('myMonitor', width=24.5, distance=60)
mon.setSizePix([1920,1080])
win = visual.Window(monitor=mon)

# define start text
my_text = visual.TextStim(win)
strt_msg = "Hello, Press any key to begin"
strt_text = visual.TextStim(win, text=strt_msg)
#-define block (start)/end text using psychopy functions
blockstart = "Press any key to continue"
block_text = visual.TextStim(win, text=blockstart)
end_msg = "You've completed this trial"
end_text = visual.TextStim(win, text=end_msg)
#-define stimuli using psychopy functions (images, fixation cross)
cross = "+"
fx_cross = visual.TextStim(win, text=cross)
my_image = visual.ImageStim(win)

# making a list of the names of the stimuli
nums = []
for i in range(10) : 
    nums.append(i+1)
pics = ["face" + (str(i).zfill(2)) + ".jpg" for i in nums]
# set block + trial quantity
nBlocks=2
nTrials=3

#=====================
#START EXPERIMENT
#=====================
#-present start message text
strt_text.draw()
win.flip() 
#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    #-present block start message
    block_text.draw()
    win.flip()
    event.waitKeys()
    #-randomize order of trials here
    numpy.random.shuffle(pics)
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        # join the path of images with the names of the files
        # iterate pics list with current trial number
        my_image.image = os.path.join(image_dir,pics[trial])
        #=====================
        #START TRIAL
        #=====================  
        # wait times are 1 second so neither of us has to sit through it
        #-draw fixation
        fx_cross.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        time.sleep(1)
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        time.sleep(1)
        
        #-draw end trial text
        end_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        time.sleep(1)
        
#======================
# END OF EXPERIMENT
#======================        
win.close()