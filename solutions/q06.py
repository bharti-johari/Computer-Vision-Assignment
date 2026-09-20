import cv2
from pathlib import Path

root = Path(__file__).resolve().parents[1]
image = cv2.imread(str(root / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
output = root / "outputs" / "q06_saved_copy.jpg"
cv2.imwrite(str(output), image)
print("Saved as:", output)
