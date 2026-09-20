import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
b, g, r = cv2.split(image)
merged = cv2.merge([b, g, r])
print("Merged image shape:", merged.shape)
cv2.imshow("Q15 - Merged Image", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
