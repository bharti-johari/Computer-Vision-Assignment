import cv2
from pathlib import Path

root = Path(__file__).resolve().parents[1]
image = cv2.imread(str(root / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
value = int(input("Enter new intensity value (0-255): "))
height, width = image.shape[:2]
if 0 <= x < width and 0 <= y < height and 0 <= value <= 255:
    image[y, x] = [value, value, value]
    output = root / "outputs" / "q12_modified_pixel.jpg"
    cv2.imwrite(str(output), image)
    print("Modified image saved to:", output)
else:
    print("Invalid coordinate or intensity value.")
