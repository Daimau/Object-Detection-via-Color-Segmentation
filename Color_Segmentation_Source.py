import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    print("Choose the color to filter:\n 1. Yellow\n 2.Red\n 3.Green\n Enter any other key to exit")
    choice = int(input("Choice: "))

    img = cv2.imread('Albaiktissue.jpg')

    if choice==1:
        yellow_filter(img)
    elif choice==2:
        red_filter(img)
    elif choice==3:
        green_filter(img)
    else:
        exit()

def yellow_filter(detectobj):
    # color detection for yellow objects

    detectobj = cv2.cvtColor(detectobj, cv2.COLOR_BGR2RGB)
    plt.imshow(detectobj)
    plt.show()

    hsv_detectobj = cv2.cvtColor(detectobj, cv2.COLOR_RGB2HSV)
    lower = np.array([23, 100, 0])
    upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv_detectobj, lower, upper)
    result = cv2.bitwise_and(detectobj, detectobj, mask=mask)

    blur = cv2.GaussianBlur(result, (7, 7), 0)
    plt.imshow(result)
    plt.show()
    return main()

def red_filter(detectobj):
    # Color detection for red objects

    detectobj = cv2.cvtColor(detectobj, cv2.COLOR_BGR2RGB)
    plt.imshow(detectobj)
    plt.show()

    hsv_detectobj = cv2.cvtColor(detectobj, cv2.COLOR_RGB2HSV)

    mask1 = cv2.inRange(hsv_detectobj, (0, 50, 20), (5, 255, 255))
    mask2 = cv2.inRange(hsv_detectobj, (175, 50, 20), (180, 255, 255))

    mask = cv2.bitwise_or(mask1, mask2)
    result = cv2.bitwise_and(detectobj, detectobj, mask=mask)

    blur = cv2.GaussianBlur(result, (7, 7), 0)
    plt.imshow(result)
    plt.show()
    return main()

def green_filter(detectobj):
    # Color detection for green objects

    detectobj = cv2.cvtColor(detectobj, cv2.COLOR_BGR2RGB)
    plt.imshow(detectobj)
    plt.show()

    hsv_detectobj = cv2.cvtColor(detectobj, cv2.COLOR_RGB2HSV)
    lower = np.array([32, 52, 72])
    upper = np.array([100, 255, 255])
    mask = cv2.inRange(hsv_detectobj, lower, upper)
    result = cv2.bitwise_and(detectobj, detectobj, mask=mask)

    blur = cv2.GaussianBlur(result, (7, 7), 0)
    plt.imshow(result)
    plt.show()
    return main()

main()