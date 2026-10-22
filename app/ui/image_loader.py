from cairosvg import svg2png
from pathlib import Path

def make_icon(svg_path, color, size, output_path):
    # Read the SVG file
    with open(svg_path, 'r') as file:
        svg_content = file.read()

    # Replace the color in the SVG content
    svg_content = svg_content.replace('currentColor', color)

    # Convert the modified SVG to PNG
    svg2png(bytestring=svg_content.encode('utf-8'), write_to=output_path, output_width=size[0], output_height=size[1])
    