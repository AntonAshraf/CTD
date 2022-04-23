import cv2

# win = r'C:\Users\anton\OneDrive\Desktop\Github\CTD\'
img = cv2.imread("C:CTD/win.jpg")

cv2.imshow("You Win", img)
cv2.waitKey(0)