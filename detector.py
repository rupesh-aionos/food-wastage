
import os
from ultralytics import YOLO

MODEL_PATH = os.getenv("MODEL_PATH", "models/best.pt")

model = YOLO(MODEL_PATH)

def detect(image_path, conf_threshold=0.25):
    results = model(image_path, conf=conf_threshold)[0]

    detections = []

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = float(box.conf[0])
        cls = int(box.cls[0])

        class_name = model.names[cls]

        detections.append({
            "bbox": [x1, y1, x2, y2],
            "confidence": conf,
            "class_name": class_name,
            "food_name": class_name   # 🔥 service-specific field
        })

    return detections