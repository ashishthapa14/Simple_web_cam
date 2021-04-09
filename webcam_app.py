import cv2

imgcapture = cv2.VideoCapture(0)
result = True

while(result):
    ret, frame = imgcapture.read()
    cv2.imwrite("Test.jpg", frame)
    result = False
    print("Image Capture..")

imgcapture.release()