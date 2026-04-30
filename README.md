# 🍽️ Food Waste Detection API (YOLOv8)

A lightweight REST API for detecting food categories (e.g., meat, vegetables, etc.) using a trained YOLOv8 model. Built with Flask and Ultralytics.

---

## 🚀 Features

* 🔍 Food detection using YOLOv8
* ⚡ Fast inference API (Flask)
* 🧪 Health check endpoint
* 📦 Easy setup with virtual environment
* 🧠 Ready for deployment (Docker/Azure compatible)

---

## 📁 Project Structure

```
food-wastage/
│
├── app.py              # Flask API server
├── detector.py         # YOLO model loading & inference
├── requirements.txt    # Dependencies
├── test.jpg            # Sample test image
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/rupesh-aionos/food-wastage.git
cd food-wastage
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate    # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### ⚠️ Important Fix (NumPy Compatibility)

This project requires:

```
numpy<2
```

Without this, you may get errors like:

* `numpy.core.multiarray failed to import`
* `_ARRAY_API not found`

---

### 4. Run the API

```
python app.py
```

---

## 🧪 API Endpoints

---

### 🔹 Health Check

```
GET /health
```

#### Test:

```
curl http://localhost:9006/health
```

#### Response:

```
{
  "status": "ok",
  "service": "food-waste",
  "model_loaded": true
}
```

---

### 🔹 Detect Food

```
POST /detect
```

#### Test:

```
curl.exe -X POST http://localhost:9006/detect -F "file=@test.jpg"
```

#### Response:

```
{
  "detections": [
    {
      "bbox": [x1, y1, x2, y2],
      "class_name": "meat",
      "confidence": 0.35,
      "food_name": "meat"
    }
  ],
  "success": true
}
```

---

## 🛠️ Tech Stack

* Python 3.10
* Flask
* Ultralytics YOLOv8
* OpenCV
* NumPy

---

## ⚡ Common Issues & Fixes

### ❌ Error: NumPy incompatibility

```
A module that was compiled using NumPy 1.x cannot be run in NumPy 2.x
```

### ✅ Fix:

```
pip uninstall numpy -y
pip install "numpy<2"
```

---

## 📌 Future Improvements

* Add confidence threshold filtering
* Add multiple object detection support
* Deploy using Docker / Azure
* Add Swagger API docs


