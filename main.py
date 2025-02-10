import cv2
from PIL import Image
from utils import get_limits


Blue = [255, 0, 0]  # BGR format
#Just for testing the camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=Blue)

    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)

    # Convert the image back to numpy array for further processing
    bbox= mask_.getbbox() # Get the bounding box of the image

    if bbox is not None:
      x1, y1,x2,y2 = bbox
      frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)  


    cv2.imshow('Test frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()