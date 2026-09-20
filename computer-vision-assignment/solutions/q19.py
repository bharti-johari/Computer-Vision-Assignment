import cv2
import numpy as np

image = np.full((256, 256), 128, dtype=np.uint8)
print("Shape:", image.shape, "Unique value:", np.unique(image))
cv2.imshow("Q19 - Constant Gray Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
