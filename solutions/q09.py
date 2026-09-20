import cv2
import matplotlib.pyplot as plt
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"))
if image is None:
    raise FileNotFoundError("Could not load image")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.axis("off")
plt.show()
