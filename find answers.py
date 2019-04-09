# import the necessary packages
import numpy as np
import cv2
from PIL import Image
import PIL.ImageGrab as ImageGrab
import PIL.ImageOps
import os
import time

global run_status
run_status = 1

if not os.path.exists('temp_photos'):
    os.makedirs('temp_photos')

box_area1 = (639,204, 730, 290) #box coordinates(x1,y1, x2,y2) to detect color of ques
box_area2 = (578,464, 623, 506) #box coordinates(x1,y1, x2,y2) to detect color of ans1
box_area3 = (744,467, 789, 509) #box coordinates(x1,y1, x2,y2) to detect color of ans2

def main():
	#os.system("echo Let's begin the Ai Game Play For Virgil")
	#os.system("pause")
	print("running in loop through while command")
	print()
	play = True
	while play:
		try:
			work()
			print()
			time.sleep(1) #waiting for 1 sec before reading second image
		except Exception as e:
			#time.sleep(4)
			play = False
			print(e)


def find_color(color_patch):
	img = cv2.imread(str('temp_photos/'+color_patch)+'.png')
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
	#print(f'int_averages: {int_averages}')
	# create a new image of the same height/width as the original
	#average_image = np.zeros((height, width, 3), np.uint8)
	average_image = np.zeros((100, 100, 3), np.uint8)
	# and fill its pixels with our average color
	average_image[:] = int_averages
	# finally, show it side-by-side with the original
	#cv2.imshow("Avg Color", np.hstack([img, average_image]))
	cv2.imwrite('temp_photos/'+str(color_patch)+"_solid.png", average_image)
	return int_averages
	#cv2.waitKey(0)

def find_pixel(color_patch):
	im = Image.open('temp_photos/'+color_patch+'.png')
	pixel = (2,2)
	color = im.getpixel(pixel)
	return color

def max_color(rgb1):
	#print('running from compare_color function')
	#print('got input as: '+str(rgb1))


	a = int(rgb1[0])
	b = int(rgb1[1])
	c = int(rgb1[2])

	if (a >= b) and (a >= c): 
		largest = 'red' 
	elif (b >= a) and (b >= c): 
		largest = 'green'
	else: 
		largest = 'blue'

	return largest

def work():
	global run_status
	#step 1 to capture the screen
	#ques = ImageGrab.grab(box_area1)
	#ans1 = ImageGrab.grab(box_area2)
	#ans2 = ImageGrab.grab(box_area3)

	#To bypass the image grab lets override and insteda of
	#taking screen shot lets just 
	test_img = Image.open(str(run_status)+".png")
	ques = test_img.crop(box_area1)
	ans1 = test_img.crop(box_area2)
	ans2 = test_img.crop(box_area3)

	ques.save('temp_photos/ques_patch.png')
	ans1.save('temp_photos/ans1_patch.png')
	ans2.save('temp_photos/ans2_patch.png')
	print("Reading image: " + str(run_status)+'.png')
	run_status += 1


	ques_patch = find_color('ques_patch')
	os.remove('temp_photos/ques_patch.png')
	ans1_patch = find_color('ans1_patch')
	os.remove('temp_photos/ans1_patch.png')
	ans2_patch = find_color('ans2_patch')
	os.remove('temp_photos/ans2_patch.png')


	ques_color = list(find_pixel('ques_patch_solid'))
	ans1_color = list(find_pixel('ans1_patch_solid'))
	ans2_color = list(find_pixel('ans2_patch_solid'))


	ques_layer = max_color(ques_color)
	ans1_layer = max_color(ans1_color)
	ans2_layer = max_color(ans2_color)

	if ans1_layer == ques_layer :
		ans = 'Left Image is Similar'
	else:
		ans = 'Right Image is Similar'

	print(ans)













#=======calling main function
if __name__ == "__main__":
	main()
