import cv2
from pathlib import Path

root = Path(__file__).resolve().parents[1]
image = cv2.imread(str(root / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
output = root / "outputs" / "q25_rotated_90.jpg"
cv2.imwrite(str(output), rotated)
print("Rotated image saved to:", output)
cv2.imshow("Q25 - Rotated 90 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
