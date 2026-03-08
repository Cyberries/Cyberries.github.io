'''
James (Juniper) Weynand
My scene is a peaceful plain with a few trees and a pond, along with some mountains in the background and a house in sight!

(No AI was used for this project (including refactoring!))

'''


# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_grass(t):
    """Draws a giant green rectangle to make the ground"""
    jump_to(t, -350, -10)
    draw_rectangle(t, 700, 340, "green")

def draw_mountain(t, x, y, size, color = "gray"):
    """Creates a mountain with optional snow"""
    jump_to(t, x, y)
    draw_triangle(t, size, color)

def draw_house(t, x, y, houseColor = "sienna", roofColor = "cornsilk"):
    """Creates a house at the given location"""
    jump_to(t, x, y)
    draw_square(t, 20, houseColor)
    jump_to(t, x-3, y)
    draw_triangle(t, 25, roofColor)
 
def draw_tree(t, x, y, trunkColor = "sienna", leafColor = "darkgreen"):
    """Draws a tree at the given location"""
    jump_to(t, x, y)
    draw_rectangle(t, 10, 50, "sienna")
    jump_to(t, x + 5, y - 20)
    draw_circle(t, 20, "darkgreen")
    
def draw_pond(t, x, y, size, color = "royalblue"):
    """Draws a pond with given location and size"""
    jump_to(t, x, y)
    draw_polygon(t, 8, size, color)

def draw_sun(t, x, y, size, color = "yellow"):
    """Draws a sun with given location and size"""
    jump_to(t, x, y)
    draw_circle(t, size, color)

#YOU MUST add function calls in this draw_scence function defintion
# to create your scence (No statements outside of function definiions)
def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # Draw Grass
    draw_grass(t)

    # Draw Mountains
    draw_mountain(t, -170, -30, 200)
    draw_mountain(t, -95, 100, 50, "white")

    draw_mountain(t, -340, -30, 300)
    draw_mountain(t, -265, 100, 150, "white")

    draw_mountain(t, -100, -45, 200)
    draw_mountain(t, -37, 65, 75, "white")

    # Draw Houses
    draw_house(t, 160, 10)
    draw_house(t, 125, 0)
    draw_house(t, 190, 5)
    draw_house(t, 175, -30)
    draw_house(t, 201, -25)

    # Draw Trees
    draw_tree(t, -120, -100)
    draw_tree(t, -150, -167)
    draw_tree(t, -180, -130)
    draw_tree(t, -90, -160)
    draw_tree(t, 140, -120)
    draw_tree(t, 120, -150)
    draw_tree(t, 25, -185)

    # Draw ponds
    draw_pond(t, 50, -100, 30)
    draw_pond(t, 95, -200, 20)
    draw_pond(t, -360, -200, 100)

    # Draw the Sun
    draw_sun(t, 250, 175, 75)

# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()
