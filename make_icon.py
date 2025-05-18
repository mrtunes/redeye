from PIL import Image, ImageDraw
import os

def create_icon(size):
    # Create a new image with a transparent background
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Calculate circle dimensions
    padding = size // 8
    circle_size = size - (2 * padding)
    
    # Draw a red circle
    draw.ellipse(
        [(padding, padding), (padding + circle_size, padding + circle_size)],
        fill=(255, 0, 0, 255)  # Red with full opacity
    )
    
    return image

# Create icons of different sizes
sizes = [16, 32, 64, 128, 256, 512, 1024]
for size in sizes:
    icon = create_icon(size)
    icon.save(f'icon.iconset/icon_{size}x{size}.png')
    # Create @2x versions
    if size <= 512:
        icon = create_icon(size * 2)
        icon.save(f'icon.iconset/icon_{size}x{size}@2x.png') 