import cv2
import numpy as np
from pathlib import Path

gray = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"), cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise FileNotFoundError("Could not load image")
quantized_4bit = (gray // 16) * 17
quantized_4bit = quantized_4bit.astype(np.uint8)
cv2.imshow("Q21 - 4-bit Quantized", quantized_4bit)
cv2.waitKey(0)
cv2.destroyAllWindows()
