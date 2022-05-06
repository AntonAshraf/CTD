import cv2
from matplotlib import image 

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

# 0 Circle - 1 Triangle - 2 Line - 3 Square
shapes = [0 for i in range(4)]
dim = ((100, 110), (100, 240), (100,380), (100, 530))

capture = cv2.VideoCapture(0)
output = cv2.imread(r'C:\Users\anton\OneDrive\Desktop\Github\CTD\#ofShapes.jpg')
cnt = 0
while True:
  isTrue, frame = capture.read()
  cv2.imshow("video",frame)
  
  if (isTrue):
    if cv2.waitKey(100) & 0xFF == ord('s'):
      resize = image_resize(frame, width=600, height=400)
      h, w = resize.shape[:2]
      crop = resize[50:h-50, 50:w-50]
      gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)      
      _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
      contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True)
        area = cv2.contourArea(contour)
        if 200 < area < 8000 :
          cv2.drawContours(crop, [contour], 0, (0, 255, 0), 1)
          cv2.drawContours(crop, [contour], 0, (0, 255, 0), 3)
          if len(approx) == 3:                # Triangle
            shapes[1] += 1
          elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            if  0.6 <= aspectRatio <= 1.4:
              shapes[3] += 1                # Square
            elif 0.0001 > aspectRatio > 0.4:
              shapes[2] += 1                # Line
          elif len(approx) == 2:
            if area < 700:
              shapes[2] += 1
          elif len(approx) > 7:
            shapes[0] += 1                  # Circle
            
      copy = output.copy()
      for j in range (4):
        cv2.putText(copy,f'{shapes[j]}', dim[j], cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
      cv2.imshow(f'Detected Shapes {cnt}', copy)
      cnt += 1
      shapes = [0 for i in range(4)]
      # cv2.imshow('thresh', thresh)
      # cv2.imshow('img with contour', crop)
      
    if cv2.waitKey(10) & 0xFF == ord('a'):
      break
  else:
    break

capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
