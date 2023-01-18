import cv2 
import numpy as np

img_name = input("Name of picture with blue ones? ")
img_name2 = input("Name of picture with red ones? ")


img = cv2.imread(img_name)
img2 = cv2.imread(img_name2)

# boundaries for the color blue
boundaries = [
    ([30, 0, 0], [255, 220, 220])
    ]

for(lower, upper) in boundaries:
    # creates numpy array from boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # finds colors in boundaries and applies a mask
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask = mask)

tot_pixel = output.size
blue_pixel = np.count_nonzero(output)
percentage = round(blue_pixel * 100 / tot_pixel, 4)

# boundaries for the color red
boundaries = [
    ([0, 0, 30], [220, 220, 255])
    ]

for(lower, upper) in boundaries:
    # creates numpy array from boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # finds colors in boundaries and applies a mask
    mask = cv2.inRange(img2, lower, upper)
    output = cv2.bitwise_and(img2, img2, mask = mask)

tot_pixel2 = output.size
red_pixel2 = np.count_nonzero(output)
percentage2 = round(red_pixel2 * 100 / tot_pixel2, 4)

living = percentage - percentage2

print("Percentage of living cells: " + str(living) + "%")

res = "Percentage of living cells: " + str(living) + "%"
with open("res.txt", 'w') as file:
	file.write(res)