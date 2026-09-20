import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
height, width, channels = image.shape
print("Height:", height)
print("Width:", width)
print("Channels:", channels)
