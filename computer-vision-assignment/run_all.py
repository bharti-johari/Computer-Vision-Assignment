import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)
img = cv2.imread(str(ROOT / 'sample.jpg'))
if img is None:
    raise FileNotFoundError('sample.jpg not found')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def save_img(name, arr, title, cmap=None):
    plt.figure(figsize=(7,5))
    if arr.ndim == 3:
        plt.imshow(cv2.cvtColor(arr, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(arr, cmap=cmap or 'gray', vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(OUT / name, dpi=140, bbox_inches='tight')
    plt.close()

def save_text(name, title, lines):
    plt.figure(figsize=(8,4.5))
    plt.axis('off')
    plt.text(0.04, 0.9, title, fontsize=16, weight='bold', va='top')
    plt.text(0.04, 0.77, '\n'.join(lines), fontsize=13, family='monospace', va='top')
    plt.tight_layout()
    plt.savefig(OUT / name, dpi=140, bbox_inches='tight')
    plt.close()

h,w,c = img.shape
save_img('q01_output.png', img, 'Q1: Read and Display Image')
save_text('q02_output.png','Q2: Image Load Check',['Image loaded successfully.'])
save_text('q03_output.png','Q3: Image Dimensions',[f'Height: {h}',f'Width: {w}',f'Channels: {c}'])
save_text('q04_output.png','Q4: Total Pixels',[f'Total pixels: {h*w}'])
save_text('q05_output.png','Q5: Image Data Type',[f'Image dtype: {img.dtype}'])
cv2.imwrite(str(OUT/'q06_saved_copy.jpg'), img)
save_text('q06_output.png','Q6: Save Image',['Saved successfully as outputs/q06_saved_copy.jpg'])
save_img('q07_output.png', gray, 'Q7: Read Directly in Grayscale')
save_img('q08_output.png', gray, 'Q8: BGR to Grayscale with cvtColor')
save_img('q09_output.png', img, 'Q9: Display with Matplotlib (Axis Hidden)')
resized = cv2.resize(img,(w//2,h//2))
save_img('q10_output.png', resized, f'Q10: Resize to 50% ({w//2} x {h//2})')
x,y=100,100
save_text('q11_output.png','Q11: Pixel Value',[f'Coordinate: ({x}, {y})',f'BGR value: {img[y,x].tolist()}'])
mod=img.copy(); mod[y,x]=[255,255,255]; cv2.imwrite(str(OUT/'q12_modified_pixel.jpg'),mod)
save_img('q12_output.png', mod, 'Q12: Modified Pixel at (100,100)')
b,g,r=img[y,x]
save_text('q13_output.png','Q13: BGR Values',[f'B: {int(b)}',f'G: {int(g)}',f'R: {int(r)}'])
bc,gc,rc=cv2.split(img)
fig,axs=plt.subplots(1,3,figsize=(12,4))
for ax,ch,title in zip(axs,[bc,gc,rc],['Blue channel','Green channel','Red channel']):
    ax.imshow(ch,cmap='gray',vmin=0,vmax=255); ax.set_title(title); ax.axis('off')
fig.tight_layout(); fig.savefig(OUT/'q14_output.png',dpi=140,bbox_inches='tight'); plt.close(fig)
merged=cv2.merge([bc,gc,rc]); save_img('q15_output.png',merged,'Q15: Merged B, G and R Channels')
save_text('q16_output.png','Q16: Min and Max Intensity',[f'Minimum intensity: {int(gray.min())}',f'Maximum intensity: {int(gray.max())}'])
save_text('q17_output.png','Q17: Mean Intensity',[f'Mean intensity: {float(gray.mean()):.2f}'])
save_text('q18_output.png','Q18: Mean and Standard Deviation',[f'Mean: {float(np.mean(gray)):.2f}',f'Standard deviation: {float(np.std(gray)):.2f}'])
const=np.full((256,256),128,dtype=np.uint8); save_img('q19_output.png',const,'Q19: 256 x 256 Image, Intensity = 128')
ramp=np.tile(np.arange(256,dtype=np.uint8),(256,1)); save_img('q20_output.png',ramp,'Q20: Grayscale Intensity Ramp 0 to 255')
q4=((gray//16)*17).astype(np.uint8); save_img('q21_output.png',q4,'Q21: 4-bit Quantized Image (16 Levels)')
q2=((gray//64)*85).astype(np.uint8); save_img('q22_output.png',q2,'Q22: 2-bit Quantized Image (4 Levels)')
down=cv2.resize(img,(w//2,h//2),interpolation=cv2.INTER_AREA); save_img('q23_output.png',down,f'Q23: Downsampled {w}x{h} -> {w//2}x{h//2}')
roi=img[80:280,80:360]; save_img('q24_output.png',roi,'Q24: Cropped ROI x=80..360, y=80..280')
rot=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE); cv2.imwrite(str(OUT/'q25_rotated_90.jpg'),rot); save_img('q25_output.png',rot,'Q25: Rotated 90 Degrees Clockwise')
print('Generated outputs for Q1-Q25 in outputs/')
