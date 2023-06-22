from ultralytics import YOLO
import cv2

model=YOLO('../YOLO-Weights/yolov8n.pt')
results=model("../Computervisionprojects-main/Computervisionprojects-main/YOLOv8-CrashCourse/Images/2.png", show=True)

cv2.waitKey(0)