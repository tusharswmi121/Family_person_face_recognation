import face_recognition
import sys
import os
import json

def load_known_faces(known_dir):
    known_encodings = []
    known_names = []

    for filename in os.listdir(known_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(known_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])
    
    return known_encodings, known_names

def match_faces(known_encodings, known_names, unknown_dir):
    results = []

    for filename in os.listdir(unknown_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(unknown_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                unknown_encoding = encodings[0]
                matches = face_recognition.compare_faces(known_encodings, unknown_encoding)
                face_distances = face_recognition.face_distance(known_encodings, unknown_encoding)
                
                best_match_index = face_distances.argmin() if matches else -1
                if best_match_index != -1 and matches[best_match_index]:
                    results.append({
                        "file": filename,
                        "match": known_names[best_match_index],
                        "confidence": float(1 - face_distances[best_match_index])
                    })
                else:
                    results.append({
                        "file": filename,
                        "match": "Unknown",
                        "confidence": 0.0
                    })
            else:
                results.append({
                    "file": filename,
                    "match": "No face detected",
                    "confidence": 0.0
                })

    return results

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python face_matcher.py <known_faces_dir> <uploaded_faces_dir>")
        sys.exit(1)

    known_dir = sys.argv[1]
    unknown_dir = sys.argv[2]

    known_encodings, known_names = load_known_faces(known_dir)
    match_results = match_faces(known_encodings, known_names, unknown_dir)
    
    print(json.dumps(match_results))
