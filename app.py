from flask import Flask, request, jsonify
import os
from detector import detect

app = Flask(__name__)

PORT = int(os.getenv("PORT", 9006))
CONF_THRESHOLD = float(os.getenv("CONF_THRESHOLD", 0.25))

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "food-waste",
        "model_loaded": True
    }), 200

@app.route("/detect", methods=["POST"])
def detect_route():
    try:
        if "file" not in request.files:
            return jsonify({
                "success": False,
                "error": "No file provided"
            }), 400

        file = request.files["file"]
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        detections = detect(file_path, CONF_THRESHOLD)

        return jsonify({
            "success": True,
            "detections": detections
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)