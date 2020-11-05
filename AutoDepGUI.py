#
# Sylvia Chin
#
# Displays a bar graph of a car's depreciated value
    # Asks user for number of years and intial value
#
from graphics import *

def carGraph():
    # Create a graphics window, width 800x600 height
    win = GraphWin("Car Depreciation Graph", 800, 600)
    
    # Ask user for initial car value in window, get keyboard input
    userask = Text(Point(690, 10), "What was your initial car value, in dollars?")
    valcar = Entry(Point(720, 40), 20)
    userask.draw(win)
    valcar.draw(win)
    
    # Ask user for number of years since car was purchased, get keyboard input
    yearask = Text(Point(670, 60),"How many years ago did you purchase your car?")
    yearval = Entry(Point(720, 90), 20)
    yearask.draw(win)
    yearval.draw(win)
    
    # Pause for entry box
    win.getMouse()

    # Get entry box values, convert to numbers
    val = eval(valcar.getText())
    years = eval(yearval.getText())
    
    # Set graphics window coordinates
        # Bottom left corner is less than 0 so graph is in screen
        # Top right corner is higher than initial car value
    win.setCoords(-2, -200, years+10, val+100)

    # Set vertical axis from 0 to initial car value
        # To get 3 other labels, divide init car value by 4 and multiply each
        # Round label value to one decimal point
    yval = ((val)/4)
    yval = round(yval, 1)
    
    Text(Point(0, 0), "0.0K").draw(win)
    Text(Point(0, yval), str(yval) + "K").draw(win)
    Text(Point(0, 2*yval), str(2*yval) + "K").draw(win)
    Text(Point(0, 3*yval), str(3*yval) + "K").draw(win)
    Text(Point(0, 4*yval), str(val) + "K").draw(win)
     
    # Draw the initial car value bar using a rectangle
      # Starts (0,0): width is one year later, height is initial value 
    bar = Rectangle(Point(2,0), Point(3, val))
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for number of years (total should be years+1 bars)
        # Use a for loop to accumulate - always offset by one year
        # Each bar is one year
    for i in range(0, years):
        val = val * 0.85
        bar = Rectangle(Point(3+i, 0), Point(3+i+1, val))
        bar.setWidth(2)
        bar.draw(win)
    
    # Once graph is displayed, create a Quit button to close the window
        # Use new years and val values to place rectangle and text 
    r = Rectangle(Point((years+10)/3,(2*val+yval)/3),
                  Point((years+10)/1.5,(2*val+yval)))
    r.setFill("red")
    r.draw(win)
    t = Text(Point((years+10)/2, (2*val+yval)/2), "QUIT")
    t.setSize(25)
    t.draw(win)
    win.getMouse()
    win.close()

carGraph()
    
