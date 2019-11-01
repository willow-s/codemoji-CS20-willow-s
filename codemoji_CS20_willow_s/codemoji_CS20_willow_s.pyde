from processing import *

# This sets up our sketch. It is the first thing that happens when we run our project, and only happens once.
def setup():
    size(300,300) # Size of our sketch
    noStroke() # Removes the outline around our shapes

#This is where we add our code for drawings and animations.
# This happens next, but loops over and over, in the same order (or sequence) that the code is listed.  
def draw():
    background(120) # set the background color to a grey

    # Emoji Head
    fill(255,218,0) # yellow
    ellipse(150, 150, 200, 200) # circle

    # Mouth
    fill(0,0,0) # black
    arc(150, 195, 100, 50, 0, PI) # semi-circle

    # Right Eye
    fill(255,255,255) # white
    ellipse(150, 145, 75, 75) # circle

    # Right Pupil
    fill(0,0,0) # black
    ellipse(150, 145, 25, 25) # circle

    # the mouseover code to help you see X and Y
    text(str((mouseX, mouseY)), mouseX, mouseY)
