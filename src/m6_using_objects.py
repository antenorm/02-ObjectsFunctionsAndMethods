"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ryan Antenore.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(500, 500)
    p1 = rg.Point(100, 100)
    p2 = rg.Point(250, 250)
    cc1 = rg.Circle(p1, 100)
    cc2 = rg.Circle(p2, 50)
    cc1.fill_color = "blue"

    cc1.attach_to(window)
    cc2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window2 = rg.RoseWindow(500, 500)

    p1 = rg.Point(100, 100)
    p2 = rg.Point(200, 200)
    p3 = rg.Point(400, 400)

    cc = rg.Circle(p1, 60)
    cc.fill_color = 'blue'

    rt = rg.Rectangle(p2, p3)
    print('', cc.outline_thickness, '\n', cc.fill_color, '\n', cc.center, '\n', p1.x, '\n', p1.y,)
    print('', rt.outline_thickness, '\n', rt.fill_color, '\n', rt.get_center())
    print('', (p2.x + p3.x)/2)
    print('', (p2.y + p3.y)/2)

    cc.attach_to(window2)
    rt.attach_to(window2)
    window2.render()
    window2.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(500, 500)
    p1 = rg.Point(100, 100)
    p2 = rg.Point(200, 200)
    p3 = rg.Point(200, 300)
    p4 = rg.Point(100, 400)

    l1 = rg.Line(p1, p2)
    l2 = rg.Line(p3, p4)
    l2.thickness = 10
    p5 = l2.get_midpoint()

    print(l2.get_midpoint(), '\n', p5.x, '\n', p5.y)
    l1.attach_to(window)
    l2.attach_to(window)

    window.render()
    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
