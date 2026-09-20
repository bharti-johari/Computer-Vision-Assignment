import cv2
import numpy as np

ramp_row = np.arange(256, dtype=np.uint8)
ramp = np.tile(ramp_row, (256, 1))
cv2.imshow("Q20 - Intensity Ramp", ramp)
cv2.waitKey(0)
cv2.destroyAllWindows()
