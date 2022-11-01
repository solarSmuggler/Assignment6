# Assignment6
Dialogue box exercises
Q2: setting session as fixed causes the session variable to be uneditable in the dialogue box

Monitor and window exercises
Q1: changing the units, if in pixels, need to consider resolution of monitor. if in cm, need to consider size of monitor in cm etc. 
Q2: yes some colors can be specified by name
    colorspace defines how the 3 numerical arguments of the color function are interpreted
    colorspace RGB = red blue green // HSV = hue, saturation, value // 
 
 Stimulus Exercises
 Q1: adding the properties units="pix" and size=(400) distorts the image. to rezise image, instead you can resize during the trial for loop so that it is image specific and doesn't make all images the same.
      at the beginning of the loop, reset the image size to the default so it doesn't keep getting bigger.
      then multiply the image width and height by a number so it scales and maintains aspect ratio.
      python can find this scaling factor for you. divide the size you want your image to be by the biggest dimension of image.size.
 Q2: you can use the height units, these are based on the size of your monitor. you can also use units pixels and print(win.size) to find your window size in pixels. Then use the size of your images (also in pixels) to figure out exactly where to put it
