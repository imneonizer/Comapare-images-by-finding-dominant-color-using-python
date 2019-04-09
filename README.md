# Comapare images using their Dominant Color
This repository is all about finding the dominant colors in images and comparing them using python.
# Working Flow
Read image for eg., `1.png` from current directory
 ```python
 from PIL import Image
original_screenshot = Image.open(str(run_status)+".png")
 ```
![Original Image](Assets/original_screenshot.png)
Crop out particular area from the image
 ```python
import PIL
box_area1 = (639,204, 730, 290)
box_area2 = (578,464, 623, 506)
box_area3 = (744,467, 789, 509)

ques = original_screenshot.crop(box_area1)
ans1 = original_screenshot.crop(box_area2)
ans2 = original_screenshot.crop(box_area3)
 ```
![Cropping Area](Assets/original_screenshot_marked.png)

After cropping the `box_area1`, `box_area2` and `box_area3` we will find the average color of that area
```python
img = cv2.imread(cropped_area.png)
height, width, _ = np.shape(img)

# calculate the average color of each row of our image
avg_color_per_row = np.average(img, axis=0)

# calculate the averages of our rows
avg_colors = np.average(avg_color_per_row, axis=0)

# avg_color is a tuple in BGR order of the average colors
# but as float values
#print(f'avg_colors: {avg_colors}')
# so, convert that array to integers
int_averages = np.array(avg_colors, dtype=np.uint8)

# create a new image of 100x100 pixels
# and fill its pixels with our average color
average_image = np.zeros((100, 100, 3), np.uint8)
average_image[:] = int_averages

# finally, save it as new image
cv2.imwrite('color_patch_solid.png", average_image)
```
Saved `color_patch_solid.png` image

![color patch solid](Assets/ques_patch_solid.png)
