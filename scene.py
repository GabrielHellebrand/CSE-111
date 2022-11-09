# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
     start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 750
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_ground(canvas, 750, 0)
    draw_sky(canvas, 750, 300)
    draw_cloud(canvas)
    draw_cloud(canvas)
    draw_pine_tree(canvas, 550, 150, 300)
    draw_pine_tree(canvas, 200, 100, 300)
    draw_pine_tree(canvas, 400, 100, 300)
    draw_grid(canvas, scene_width, scene_height, 50)

    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    scene_height = 700
    scene_width = 750
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 000, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height):
    scene_height = 100
    scene_width = 750
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 000, 750,
        scene_width, scene_height / 3, width=0, fill="forest green")

def draw_cloud(canvas):
    draw_oval(canvas, 100, 400, 200, 350, fill="white", outline="white")
    draw_oval(canvas, 120, 430, 200, 350, fill="white", outline="white")
    draw_oval(canvas, 150, 460, 250, 350, fill="white", outline="white")
    draw_oval(canvas, 300, 400, 200, 350, fill="white", outline="white")
    draw_oval(canvas, 320, 430, 200, 350, fill="white", outline="white")
    draw_oval(canvas, 350, 460, 250, 350, fill="white", outline="white")



def draw_pine_tree(canvas, center_x, bottom, height):
    # Draw the trunk of the tree
    trunk_width = height / 10
    trunk_height = height / 8

    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill = "tan4")

    # Draw the skirt of the tree
    skirt_width = height / 2
    skirt_left  = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2

    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill = "forest green")

def draw_grid(canvas, width, height, interval):
    # draw vertical lines
    label_y = 15
    for x in range (interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

# draw horizontal lines
    label_x = 15
    for y in range (interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

# Call the main function so that
# this program will start executing.
main()