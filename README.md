# 👨‍👩‍👧‍👦Family Person Face Recognition 

Identify whether an uploaded face photo matches any pre-stored family member.
Full-stack app: React (UI) → Spring Boot (API) → Python + face_recognition/OpenCV (matching) → MySQL (optional history).

# ✨ What it does

Compares a person’s face image with known family photos stored in a folder (backend/x).<br/>
Returns Match / No Match, the matched person’s name, and a confidence score.<br/>

(Optional) Logs results to MySQL for a simple history/audit page.

# 🧱 Tech Stack

a) Frontend: React + Axios<br/>
b) Backend: Java 17, Spring Boot (Web, JPA), REST<br/>
c) Face Matching Service: Python (Flask), face_recognition (dlib), NumPy<br/>
d) Database (optional): MySQL (via Spring Data JPA/Hibernate)<br/>

# 📁 Project Structure

```
data-integrity-project/
├── backend/
│   ├── src/main/java/com/example/backend/
│   │   ├── BackendApplication.java
│   │   ├── controller/
│   │   │   └── FileController.java          # POST /api/files/upload -> calls Python API
│   │   ├── service/
│   │   │   └── FileService.java             # (optional) DB save/lookup
│   │   ├── model/
│   │   │   └── FileRecord.java              # (optional) entity for history
│   │   └── repository/
│   │       └── FileRecordRepository.java    # (optional) Spring Data JPA
│   ├── src/main/resources/
│   │   └── application.properties
│   ├── x/                                   # ✅ known family faces (person1.jpg ... person5.jpg)
│   ├── y/                                   # (optional) uploaded images
│   └── pom.xml
│
├── frontend-react/
│   ├── src/
│   │   ├── api/api.js
│   │   ├── components/FileUpload.js
│   │   ├── components/ResultDisplay.js
│   │   └── pages/Home.js
│   └── package.json
│
└── face_match_api.py                         # Python Flask face-match microservice
```

# ⚙️ Prerequisites

a) Java 17, Maven 3.9+<br/>
b) Node 18+ / npm 9+<br/>
c) Python 3.10+ (Apple Silicon users: prefer a venv)<br/>
(Optional) MySQL 8+<br/>

# How It Works (1-minute)

a) React lets the user choose a photo and sends it as multipart/form-data.<br/>
b) Spring Boot receives the file, forwards it to the Python service.<br/>
c) Flask + face_recognition compares with all faces in backend/x/:<br/>
d) Extracts encodings (128-D vectors) and computes distance to each known face.<br/>
e) Picks best match and returns name + confidence.<br/>
f) Spring Boot relays the result to the React UI (and optionally saves it).<br/>
