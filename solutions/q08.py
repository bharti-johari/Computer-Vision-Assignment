import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Q8 - Converted Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
