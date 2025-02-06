# **Safeguarding Stories: AI for Intellectual Property Protection (AIML)**

**Problem Statement:**
Disney's vast library of intellectual property, including movies, TV shows, and characters, is a prime target for cyberattacks and piracy.Unauthorized access and distribution of this content can lead to significant financial losses and damage to the brand.

**Objective:**
Participants are tasked with developing AI-driven solutions to protect Disney's intellectual property from cyber threats. Solutions should include real-time monitoring, automated takedown requests, and predictive analytics to identify and mitigate piracy risks.

## **Overview**  
Safeguarding Stories: AI for Intellectual Property Protection is an advanced AI-driven system designed to detect copyright violations, unauthorized content, and intellectual property misuse on YouTube. By leveraging deep learning, NLP, and computer vision techniques, the system enables real-time monitoring, automated DMCA takedown requests, and predictive piracy analytics.  

## **Table of Contents**  
- [Overview](#overview)  
- [Table of Contents](#table-of-contents)  
- [Project Structure (AIML)](#project-structure-aiml)  
- [Features (AIML)](#features-aiml)  
- [Project Structure (Frontend)](#project-structure-frontend)  
- [Features (Frontend)](#features-frontend)  
- [Project Structure (Backend)](#project-structure-backend)  
- [Features (Backend)](#features-backend)  
- [Configuration](#configuration)  
- [Usage](#usage)  
  - [Basic Usage](#basic-usage)  
  - [Running Tests](#running-tests)  
- [Tech Stack](#tech-stack)  
- [Team](#team)  
- [License](#license)  
- [Contributing](#contributing)  

---

## **Project Structure (AIML)**  
```
📦 AI-ML  
 ┣ 📂 data/  
 ┃ ┣ 📜 raw_videos.csv  
 ┃ ┣ 📜 processed_videos.json  
 ┃ ┣ 📂 logs/  
 ┃ ┃ ┗ 📜 scraper.log  
 ┃ ┣ 📂 models/  
 ┃ ┃ ┣ 📜 yolo_weights.onnx  
 ┃ ┃ ┗ 📜 audio_fingerprint.pkl  
 ┃ ┗ 📜 dmca_requests.json  
 ┣ 📂 src/  
 ┃ ┣ 📂 api/  
 ┃ ┃ ┣ 📜 youtube_scraper.py  
 ┃ ┃ ┣ 📜 dmca_handler.py  
 ┃ ┃ ┗ 📜 ai_integration.py  
 ┃ ┣ 📂 processing/  
 ┃ ┃ ┣ 📜 video_downloader.py  
 ┃ ┃ ┣ 📜 frame_extractor.py  
 ┃ ┃ ┗ 📜 audio_extractor.py  
 ┃ ┣ 📂 ai/  
 ┃ ┃ ┣ 📜 object_detection.py  
 ┃ ┃ ┣ 📜 audio_analysis.py  
 ┃ ┃ ┗ 📜 feature_extraction.py  
 ┃ ┣ 📂 storage/  
 ┃ ┃ ┗ 📜 firestore_db.py  
 ┃ ┣ 📜 main.py  
 ┃ ┣ 📜 config.py  
 ┃ ┗ 📜 utils.py  
 ┣ 📂 notebooks/  
 ┃ ┗ 📜 exploratory_analysis.ipynb  
 ┣ 📂 tests/  
 ┃ ┣ 📜 test_scraper.py  
 ┃ ┣ 📜 test_object_detection.py  
 ┃ ┗ 📜 test_firestore_db.py  

```
## **Features (AIML)**  
✔ Detects Disney characters and logos using AI  
✔ Extracts audio fingerprints for copyrighted sound detection  
✔ Generates automated DMCA takedown requests  
✔ Stores analyzed video data in Firestore  
✔ Provides real-time content monitoring  

---

## **Project Structure (Frontend)**  
```
📦 Frontend  
 ┣ 📂 public/  
 ┃ ┗ 📜 index.html  
 ┣ 📂 src/  
 ┃ ┣ 📂 components/  
 ┃ ┃ ┣ 📜 Navbar.jsx  
 ┃ ┃ ┣ 📜 VideoCard.jsx  
 ┃ ┃ ┗ 📜 DMCAForm.jsx  
 ┃ ┣ 📂 pages/  
 ┃ ┃ ┣ 📜 Home.jsx  
 ┃ ┃ ┣ 📜 VideoAnalysis.jsx  
 ┃ ┃ ┗ 📜 DMCARequests.jsx  
 ┃ ┣ 📂 services/  
 ┃ ┃ ┣ 📜 api.js  
 ┃ ┃ ┗ 📜 auth.js  
 ┃ ┣ 📂 context/  
 ┃ ┃ ┗ 📜 AppContext.js  
 ┃ ┣ 📂 styles/  
 ┃ ┃ ┗ 📜 styles.css  
 ┃ ┣ 📜 App.jsx  
 ┃ ┗ 📜 index.js  
 ┣ 📜 package.json  
 ┣ 📜 .env  
 ┣ 📜 README.md  

```
## **Features (Frontend)**  
✔ User-friendly dashboard to track detected copyright violations  
✔ Form to submit DMCA takedown requests  
✔ Real-time notifications on video status  
✔ Dark and light mode UI  

---

## **Project Structure (Backend)**  
```
📦 Backend  
 ┣ 📂 controllers/  
 ┃ ┣ 📜 videoController.js  
 ┃ ┣ 📜 aiController.js  
 ┃ ┗ 📜 dmcaController.js  
 ┣ 📂 models/  
 ┃ ┗ 📜 videoModel.js  
 ┣ 📂 routes/  
 ┃ ┣ 📜 videoRoutes.js  
 ┃ ┣ 📜 aiRoutes.js  
 ┃ ┗ 📜 dmcaRoutes.js  
 ┣ 📂 middleware/  
 ┃ ┣ 📜 authMiddleware.js  
 ┃ ┗ 📜 errorHandler.js  
 ┣ 📂 config/  
 ┃ ┗ 📜 db.js  
 ┣ 📂 services/  
 ┃ ┣ 📜 aiService.js  
 ┃ ┗ 📜 dmcaService.js  
 ┣ 📂 storage/  
 ┃ ┗ 📜 upload.js  
 ┣ 📜 app.js  
 ┣ 📜 .env  
 ┣ 📜 package.json
```

## **Features (Backend)**  
✔ RESTful API for AI processing and takedown management  
✔ Secure authentication using JWT  
✔ Database integration with Firestore  
✔ Handles YouTube video scraping and processing  

---
## Team Members

| Name                | Role                        | Description                | Contact                        |
|---------------------|-----------------------------|----------------------------|--------------------------------|
| Shaktidhar Gupta    | Leader & AIML Engineer       | Leads the team and works on AI/ML tasks | [sktigpta@gmail.com](mailto:sktigpta@gmail.com) |
| Satyam Kumar        | Backend Developer           | Handles the server-side and database management | [satyam@example.com](mailto:satyam@example.com) |
| Saurav Kumar        | Frontend Designer and UI/UX engg        | Works on the user interface design | [sauravkumar9447@gmail.com](mailto:sauravkumar9447@gmail.com) |
| Rishi Srestha       | Frontend Designer & Documentation | Designs the UI and handles project documentation | [rishi@example.com](mailto:rishi@example.com) |
