import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
height, width = image.shape[:2]
if 0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height:
    roi = image[y1:y2, x1:x2]
    cv2.imshow("Q24 - ROI", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Invalid ROI coordinates.")
