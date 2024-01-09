from ultralytics import YOLO
import cv2


model = YOLO('yolov8n.pt')
result = model("images/1.jpg",show=True)

cv2.waitKey(0)

