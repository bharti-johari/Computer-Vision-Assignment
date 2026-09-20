import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
height, width = image.shape[:2]
resized = cv2.resize(image, (width // 2, height // 2))
print("Original:", (width, height))
print("Resized:", (resized.shape[1], resized.shape[0]))
cv2.imshow("Q10 - 50 Percent", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
