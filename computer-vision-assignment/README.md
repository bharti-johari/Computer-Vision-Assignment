# Computer Vision – Day 1 Assignment
> **Sample image:** The assignment outputs in this repository were generated from the provided real-world `sample.jpg` (forest photograph), not from a synthetic generated image.

Complete solutions for the **25 Python + OpenCV coding questions** in the provided assignment.

## Topics covered
- Basic image handling
- Pixel and image representation
- Sampling and quantization
- Geometric operations

## Requirements

```bash
pip install -r requirements.txt
```

Recommended: Python 3.10+.

## Project structure

```text
computer-vision-day1-assignment/
├── README.md
├── requirements.txt
├── sample.jpg
├── generate_sample.py
├── run_all.py
├── solutions/
│   ├── q01.py
│   ├── q02.py
│   ├── ...
│   └── q25.py
└── outputs/
    ├── q01_output.png
    ├── ...
    └── q25_output.png
```

> Some scripts use `cv2.imshow()`. Run those locally in VS Code/PyCharm because a GUI window is required.

---

## Q1. Read an image using OpenCV and display it
**Approach:** Use `cv2.imread()` to read `sample.jpg`, then `cv2.imshow()` to display it.

**Code:** `solutions/q01.py`

**Important functions:** `cv2.imread()`, `cv2.imshow()`, `cv2.waitKey()`, `cv2.destroyAllWindows()`.

**Observation:** OpenCV reads a normal color image as a BGR NumPy array.

**Output:** `outputs/q01_output.png`

## Q2. Check whether an image loaded successfully
**Approach:** After reading the image, check whether the returned object is `None`.

**Code:** `solutions/q02.py`

**Important functions:** `cv2.imread()`.

**Observation:** `cv2.imread()` returns `None` when the file cannot be read.

**Output:** `outputs/q02_output.png`

## Q3. Print height, width, and number of channels
**Approach:** Use the image array's `shape` property.

**Code:** `solutions/q03.py`

**Important concept:** For a color image, `image.shape` is `(height, width, channels)`.

**Observation:** The provided sample image is 1365 × 2048 with 3 color channels.

**Output:** `outputs/q03_output.png`

## Q4. Calculate total number of pixels
**Approach:** Multiply image height by image width.

**Code:** `solutions/q04.py`

**Important concept:** Total pixels = `height × width`; channels are not multiplied when counting spatial pixels.

**Output:** `outputs/q04_output.png`

## Q5. Print the image matrix data type
**Approach:** Print `image.dtype`.

**Code:** `solutions/q05.py`

**Important concept:** Standard 8-bit images are usually stored as `uint8` values in the range 0–255.

**Output:** `outputs/q05_output.png`

## Q6. Save the image with another filename
**Approach:** Read the original image and save a copy using `cv2.imwrite()`.

**Code:** `solutions/q06.py`

**Important functions:** `cv2.imread()`, `cv2.imwrite()`.

**Observation:** The pixel data can be written to another image file without changing the original.

**Output:** `outputs/q06_output.png`, `outputs/q06_saved_copy.jpg`

## Q7. Read an image directly in grayscale
**Approach:** Pass `cv2.IMREAD_GRAYSCALE` to `cv2.imread()`.

**Code:** `solutions/q07.py`

**Important function:** `cv2.imread(path, cv2.IMREAD_GRAYSCALE)`.

**Observation:** The resulting array has only two dimensions: height and width.

**Output:** `outputs/q07_output.png`

## Q8. Convert a color image to grayscale
**Approach:** Read the color image and use `cv2.cvtColor()` with `cv2.COLOR_BGR2GRAY`.

**Code:** `solutions/q08.py`

**Important function:** `cv2.cvtColor()`.

**Observation:** Grayscale conversion reduces three color channels to one intensity channel.

**Output:** `outputs/q08_output.png`

## Q9. Display an image using Matplotlib and hide the axis
**Approach:** Convert BGR to RGB before displaying with Matplotlib, then call `plt.axis('off')`.

**Code:** `solutions/q09.py`

**Important functions:** `cv2.cvtColor()`, `plt.imshow()`, `plt.axis()`.

**Observation:** Matplotlib expects RGB ordering while OpenCV uses BGR.

**Output:** `outputs/q09_output.png`

## Q10. Resize an image to 50% width and height
**Approach:** Calculate half the original width and height and call `cv2.resize()`.

**Code:** `solutions/q10.py`

**Important function:** `cv2.resize()`.

**Observation:** Reducing both width and height by half reduces the number of pixels to one fourth.

**Output:** `outputs/q10_output.png`

## Q11. Access a pixel at a user-provided coordinate
**Approach:** Read `(x, y)` from the user and access the NumPy array as `image[y, x]`.

**Code:** `solutions/q11.py`

**Important concept:** NumPy uses row first, so coordinate `(x, y)` is accessed as `[y, x]`.

**Observation:** A color pixel returns three BGR values.

**Output example:** `outputs/q11_output.png`

## Q12. Modify a selected pixel and save the image
**Approach:** Validate coordinates and intensity, assign a new pixel value, then save the modified image.

**Code:** `solutions/q12.py`

**Important concepts:** NumPy indexing, `cv2.imwrite()`.

**Observation:** A single pixel can be changed directly because an OpenCV image is a mutable NumPy array.

**Output:** `outputs/q12_output.png`, `outputs/q12_modified_pixel.jpg`

## Q13. Print B, G, and R values of a selected pixel
**Approach:** Read a pixel and unpack it as `b, g, r`.

**Code:** `solutions/q13.py`

**Important concept:** OpenCV color channel order is BGR, not RGB.

**Output example:** `outputs/q13_output.png`

## Q14. Split a color image into B, G, and R channels
**Approach:** Call `cv2.split(image)` and display the returned channel matrices.

**Code:** `solutions/q14.py`

**Important function:** `cv2.split()`.

**Observation:** Each channel is a grayscale matrix representing the intensity of one color component.

**Output:** `outputs/q14_output.png`

## Q15. Merge three image channels into one color image
**Approach:** Split the image and combine the channels again with `cv2.merge([b, g, r])`.

**Code:** `solutions/q15.py`

**Important function:** `cv2.merge()`.

**Observation:** Merging channels in the original BGR order reconstructs the original color appearance.

**Output:** `outputs/q15_output.png`

## Q16. Find minimum and maximum grayscale intensity
**Approach:** Load a grayscale image and use NumPy's `min()` and `max()` methods.

**Code:** `solutions/q16.py`

**Important concepts:** `gray.min()`, `gray.max()`.

**Observation:** These values show the darkest and brightest intensities present in the image.

**Output:** `outputs/q16_output.png`

## Q17. Calculate mean grayscale intensity
**Approach:** Use `gray.mean()`.

**Code:** `solutions/q17.py`

**Important concept:** The mean gives the average brightness of the image.

**Output:** `outputs/q17_output.png`

## Q18. Calculate mean and standard deviation
**Approach:** Use `np.mean()` and `np.std()` on the grayscale matrix.

**Code:** `solutions/q18.py`

**Important functions:** `np.mean()`, `np.std()`.

**Observation:** Mean describes average brightness; standard deviation describes spread/contrast of intensity values.

**Output:** `outputs/q18_output.png`

## Q19. Create a 256 × 256 grayscale image with intensity 128
**Approach:** Use `np.full((256, 256), 128, dtype=np.uint8)`.

**Code:** `solutions/q19.py`

**Important function:** `np.full()`.

**Observation:** Every pixel has the same middle-gray intensity, so the image is uniformly gray.

**Output:** `outputs/q19_output.png`

## Q20. Create a grayscale intensity ramp from 0 to 255
**Approach:** Create values `0...255` with `np.arange()` and repeat the row using `np.tile()`.

**Code:** `solutions/q20.py`

**Important functions:** `np.arange()`, `np.tile()`.

**Observation:** The image gradually changes from black to white across its width.

**Output:** `outputs/q20_output.png`

## Q21. Convert an 8-bit grayscale image to 4-bit quantization
**Approach:** Reduce 256 possible intensity values to 16 levels. The code uses integer division by 16, then maps each level across the 0–255 display range.

**Code:** `solutions/q21.py`

**Important concept:** 4-bit representation provides `2^4 = 16` intensity levels.

**Observation:** Some fine intensity variation is removed and banding becomes more visible.

**Output:** `outputs/q21_output.png`

## Q22. Convert an 8-bit grayscale image to 2-bit quantization
**Approach:** Reduce 256 values to 4 levels and map them to approximately `0, 85, 170, 255`.

**Code:** `solutions/q22.py`

**Important concept:** 2-bit representation provides `2^2 = 4` intensity levels.

**Observation:** Much more visual detail is lost than in 4-bit quantization.

**Output:** `outputs/q22_output.png`

## Q23. Downsample the image by a factor of 2
**Approach:** Resize to half the width and half the height using `cv2.INTER_AREA`.

**Code:** `solutions/q23.py`

**Important functions:** `cv2.resize()`, `cv2.INTER_AREA`.

**Observation:** Spatial resolution is reduced from 2048 × 1365 to 1024 × 682 for the provided sample image.

**Output:** `outputs/q23_output.png`

## Q24. Crop a rectangular ROI using user-provided coordinates
**Approach:** Read `(x1, y1)` and `(x2, y2)`, validate them, then use NumPy slicing: `image[y1:y2, x1:x2]`.

**Code:** `solutions/q24.py`

**Important concept:** Cropping does not require a special OpenCV function because image arrays support slicing.

**Observation:** Only the selected rectangle remains in the ROI image.

**Output example:** `outputs/q24_output.png`

## Q25. Rotate an image by 90 degrees and save it
**Approach:** Use `cv2.rotate()` with `cv2.ROTATE_90_CLOCKWISE`, display it, then save it.

**Code:** `solutions/q25.py`

**Important functions:** `cv2.rotate()`, `cv2.imwrite()`.

**Observation:** After a 90° rotation, width and height exchange positions.

**Output:** `outputs/q25_output.png`, `outputs/q25_rotated_90.jpg`

---

## Generate all output images

Run:

```bash
python run_all.py
```

This creates representative output screenshots for all 25 questions in the `outputs/` folder.

## Run one solution

Example:

```bash
python solutions/q03.py
```

For questions requiring input, such as Q11, Q12, Q13, and Q24, enter valid coordinates within the image dimensions.

## Viva quick points
- OpenCV normally reads images in **BGR** order.
- `image.shape` for a color image is `(height, width, channels)`.
- A grayscale image normally has one intensity value per pixel from 0 to 255.
- NumPy image indexing is `[row, column]`, equivalent to `[y, x]`.
- 4-bit quantization gives 16 intensity levels; 2-bit gives 4.
- Downsampling reduces spatial resolution; quantization reduces intensity resolution.
- Cropping is performed efficiently using NumPy slicing.
