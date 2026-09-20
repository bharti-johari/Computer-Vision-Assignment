import cv2
from pathlib import Path

image_path = Path(__file__).resolve().parents[1] / "sample.jpg"
image = cv2.imread(str(image_path))
if image is None:
    print(f"Error: unable to load image from {image_path}")
else:
    print("Image loaded successfully.")
