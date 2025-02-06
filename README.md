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
📦 backend  
 ┣ 📂 config/
 ┣  ┣ 📂 db/
 ┣  ┗ 📂 email/
 ┣ 📂 controllers/
 ┣ 📂 roots/
 ┣ 📂 models/
 ┣ 📜 index.js
 ┗ 📜 app.js
```

## Features
- Real-time YouTube video monitoring
- AI-powered content analysis using OpenCV
- Automated detection of Disney characters and logos
- Integration with YouTube Data API
- Firestore database for data storage
- User-friendly dashboard for monitoring

<!-- ## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/youtube-ai-analyzer.git
cd youtube-ai-analyzer
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your API keys
``` -->

## Configuration
1. YouTube Data API Setup:
   - Create a Google Cloud Project
   - Enable YouTube Data API
   - Generate API key

2. Firebase Setup:
   - Create a Firebase project
   - Enable Firestore
   - Download service account key


### Core Components

| File | Description | Function |
|------|-------------|-----------|
| `src/main.py` | Entry point | Orchestrates the entire application flow |
| `src/config.py` | Configuration | Stores API keys and global settings |
| `src/utils.py` | Utilities | Contains helper functions |

### API Components

| File | Description | Function |
|------|-------------|-----------|
| `src/api/youtube_scraper.py` | YouTube Scraper | Fetches videos using YouTube Data API |

### Processing Components

| File | Description | Function |
|------|-------------|-----------|
| `src/processing/video_downloader.py` | Video Downloader | Downloads YouTube videos for analysis |
| `src/processing/frame_extractor.py` | Frame Extractor | Extracts frames from videos |

### AI Components

| File | Description | Function |
|------|-------------|-----------|
| `src/ai/object_detection.py` | Object Detection | Detects Disney characters and logos |
| `src/ai/feature_extraction.py` | Feature Extraction | Extracts features from video frames |

### Storage Components

| File | Description | Function |
|------|-------------|-----------|
| `src/storage/firestore_db.py` | Database Handler | Manages Firestore operations |

## Usage

### Basic Usage
```python
from src.main import YouTubeAnalyzer

analyzer = YouTubeAnalyzer()
analyzer.start_monitoring()
```

### Running Tests
```bash
python -m pytest tests/
```

## Tech Stack
- Python 3.8+
- OpenCV for video analysis
- TensorFlow/YOLO for object detection
- Firebase Firestore for data storage
- YouTube Data API v3
- Flutter/React for dashboard

## Team
**Tech-NO-Logic**: A dynamic team of innovators uniting tech and creativity to solve real-world problems with cutting-edge solutions. Passion meets logic for impactful change. 🚀

## License
no license till now

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request