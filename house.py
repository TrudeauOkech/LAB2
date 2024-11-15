import cairo

# Create the surface and context
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 400, 300)
ctx = cairo.Context(surface)

# Set background to white
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Set line color to red and line width
ctx.set_source_rgb(1, 0, 0)  # Red color
ctx.set_line_width(2)

# Draw the parallelogram with refined angles and proportions
ctx.move_to(80, 180)     # Starting point (bottom left)
ctx.line_to(160, 120)    # Top left line
ctx.line_to(320, 120)    # Top horizontal line
ctx.line_to(200, 190)    # Bottom line
ctx.line_to(80, 180)     # Close the shape

# Stroke the path
ctx.stroke()

# Save the result
surface.write_to_png('house_step1a.png')