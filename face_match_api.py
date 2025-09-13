from flask import Flask, request, jsonify
import face_recognition
import numpy as np
import os

app = Flask(__name__)

# Path to known faces directory
KNOWN_DIR = "/Users/tusharswami/Desktop/data-integrity-project/backend/x"

def load_known_faces(known_dir):
    known_encodings = []
    known_names = []

    for filename in os.listdir(known_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(known_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])

    return known_encodings, known_names

@app.route('/compare_faces', methods=['POST'])
def compare_faces():
    try:
        # Load known faces from the directory
        known_encodings, known_names = load_known_faces(KNOWN_DIR)

        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        uploaded_file = request.files['file']
        uploaded_image = face_recognition.load_image_file(uploaded_file)
        uploaded_encodings = face_recognition.face_encodings(uploaded_image)

        if not uploaded_encodings:
            return jsonify({'error': 'No face found in uploaded image'}), 400

        uploaded_encoding = uploaded_encodings[0]

        matches = face_recognition.compare_faces(known_encodings, uploaded_encoding)
        face_distances = face_recognition.face_distance(known_encodings, uploaded_encoding)

        if len(matches) > 0 and any(matches):
            best_match_index = np.argmin(face_distances)
            return jsonify({
                "match": True,
                "matched_with": known_names[best_match_index],
                "confidence": float(1 - face_distances[best_match_index])
            })
        else:
            return jsonify({
                "match": False,
                "matched_with": "Unknown",
                "confidence": 0.0
            })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
