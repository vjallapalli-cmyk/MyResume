from PIL import Image, ImageEnhance, ImageFilter
import os

# Path to the original image
image_path = r"C:\Users\Thulisha reddy\OneDrive\Desktop\rugved\WhatsApp Image 2026-01-21 at 21.44.00.jpg.jpeg"

# Output path
output_path = r"C:\Users\Thulisha reddy\OneDrive\Desktop\rugved\profile_enhanced.jpg"

# Open the image
img = Image.open(image_path)

# Enhance color balance
enhancer = ImageEnhance.Color(img)
img = enhancer.enhance(1.2)  # Slightly increase color saturation

# Enhance brightness
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(1.1)  # Slightly brighter

# Enhance contrast
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.1)  # Slightly more contrast

# Sharpen the image
img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))

# Crop to square (center crop)
width, height = img.size
min_side = min(width, height)
left = (width - min_side) / 2
top = (height - min_side) / 2
right = (width + min_side) / 2
bottom = (height + min_side) / 2
img = img.crop((left, top, right, bottom))

# Resize to 400x400 for profile
img = img.resize((400, 400), Image.Resampling.LANCZOS)

# Save the enhanced image
img.save(output_path, 'JPEG', quality=95)

print("Image enhanced and saved as profile_enhanced.jpg")