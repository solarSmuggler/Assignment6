# import functions
from psychopy import gui, visual, monitors
from datetime import datetime
import os
main_dir = os.getcwd()

#========================
# DIALOGUE BOX EXERCISES
#========================

# create dictionary for subject info
exp_info = {'session':1,'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':'-'}

# dialogue box for subject info
my_dlg = gui.DlgFromDict(exp_info,title="Subject Info", fixed=['session'],order=['session','subject_nr','age','gender','handedness'], show=False)
# setting session as fixed causes the session variable to be uneditable in the dialogue box

# get date and time
date = datetime.now()
# add date to the dictionary and make it look nice
exp_info['date'] = str(date.day) + '/' + str(date.month) + '/' + str(date.year)

# print statement
print("All variables have been created! Now ready to show the dialog box!")

# show dialogue box
my_dlg.show()

# creat unique filename for data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)
# directory to save the file in
sub_dir = os.path.join(main_dir,'sub_info',filename)

#==============================
# MONITOR + WINDOWS EXERCISES
#==============================
mon = monitors.Monitor('myMonitor', width=24.5, distance=60)
mon.setSizePix([1920,1080])
colorspace = 'hsv'
win = visual.Window(monitor=mon, fullscr=False, units='pix', size=(1000,800), color=['cadetblue'])
# changing the units, if in pixels, need to consider resolution of monitor. if in cm, need to consider size of monitor in cm etc. 
# yes colors can be specified by name
# colorspace defines how the 3 numerical arguments of the color function are interpreted
     # colorspace RGB = red blue green // HSV = hue, saturation, value // 