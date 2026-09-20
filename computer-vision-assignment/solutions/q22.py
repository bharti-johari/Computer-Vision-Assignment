import cv2
import numpy as np
from pathlib import Path

gray = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"), cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise FileNotFoundError("Could not load image")
quantized_2bit = (gray // 64) * 85
quantized_2bit = quantized_2bit.astype(np.uint8)
cv2.imshow("Q22 - 2-bit Quantized", quantized_2bit)
cv2.waitKey(0)
cv2.destroyAllWindows()
