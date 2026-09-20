import cv2
import numpy as np
from pathlib import Path

gray = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample.jpg"), cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise FileNotFoundError("Could not load image")
mean = np.mean(gray)
std_dev = np.std(gray)
print("Mean:", float(mean))
print("Standard deviation:", float(std_dev))
