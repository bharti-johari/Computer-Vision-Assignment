import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
height, width = image.shape[:2]
if 0 <= x < width and 0 <= y < height:
    b, g, r = image[y, x]
    print("B:", int(b), "G:", int(g), "R:", int(r))
else:
    print("Coordinates are outside the image.")
