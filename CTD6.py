import cv2 
import numpy as np

# 0 Circle - 1 Triangle - 2 Line - 3 Square
shapes = [0 for i in range(4)]
dim = ((100, 110), (100, 240), (100,380), (100, 530))

capture = cv2.VideoCapture(0)
output = cv2.imread(r'C:\Users\anton\OneDrive\Desktop\Github\CTD\#ofShapes.jpg')

i = 0
while True:
  isTrue, frame = capture.read()
  cv2.imshow("video",frame)
  
  if (isTrue):
    if cv2.waitKey(10) & 0xFF == ord('s'):
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      
      _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
      contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      for contour in contours:
        if i == 0:
          i = 1
          continue
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        # cv2.drawContours(frame, [contour], 0, (0, 255, 0), 1)
        if len(approx) == 1:      # Line
          shapes[2] += 1
        elif len(approx) == 3:    # Triangle
          shapes[1] += 1
        elif len(approx) == 4:    # Square
          shapes[3] += 1    
        else:                     # Circle
          shapes[0] += 1
          
      for j in range (4):
        cv2.putText(output,f'{shapes[j]}', dim[j], cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
      break

    if cv2.waitKey(10) & 0xFF == ord('a'):
      break
  else:
    break

capture.release()
cv2.destroyAllWindows()
cv2.imshow('Detected Shapes', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
