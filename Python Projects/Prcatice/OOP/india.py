from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Load your image (make sure the path matches your file)
image_path = "your_image_path.png"  # Replace with your actual image path
base_image = Image.open(image_path).convert("RGBA")

# Create a drawable object
draw = ImageDraw.Draw(base_image)

# Use default font
font = ImageFont.load_default()

# Approximate (x, y) positions for each location on the map
locations = {
    "Udhampur Airbase": (310, 100),
    "Pathankot Airbase": (280, 130),
    "Drangyari": (330, 110),
    "Uri": (300, 105),
    "Nagrota (BrahMos)": (315, 115),
    "Beas (BrahMos)": (270, 160),
    "Adampur (S-400)": (260, 170),
    "Bhuj Airbase": (180, 290),
}

# Draw red dots and labels for each location
for name, (x, y) in locations.items():
    draw.ellipse((x-3, y-3, x+3, y+3), fill="red")
    draw.text((x + 5, y - 5), name, fill="black", font=font)

# Show the marked image
plt.figure(figsize=(10, 10))
plt.imshow(base_image)
plt.axis('off')
plt.title("Marked Defense Sites on India Map")
plt.show()
