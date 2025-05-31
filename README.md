# Flask Photo Gallery Application

## Overview
This project is a **Flask-based image gallery** that allows users to:
- Create, Read, Update, and Delete (CRUD)** galleries.
- Upload photos with captions** inside galleries.
- Manage user sessions** (login/logout).
- Secure file handling** (`secure_filename`).
- Provide a simple UI for managing galleries**.

## Features
- User Authentication** – Login & Logout  
- Gallery Management (CRUD) – Add, Edit, Delete galleries  
- Photo Uploading– Securely store images  
- Mobile-Friendly UI – Uses Bootstrap  
- Session Management – Admin control over galleries  

---

##Installation & Setup

### Clone the Repository
```sh
git clone https://github.com/your-repo/photo-gallery-python-flask.git
cd photo-gallery-python-flask

Install Dependencies
pip install -r requirements.txt

Run the Flask Server
python main.py

The app will be accessible at http://127.0.0.1:5000


Changes from Original Version

1. Enhanced REST API Functionality
Implemented full CRUD operations for galleries and photos.

Improved error handling with proper HTTP status codes (200, 400, 404).

Ensured consistent JSON request/response format.

New API documentation added to explain each route and its expected behavior.

2. Unit Testing Integration
Added pytest-based unit tests covering all CRUD operations.

Achieved near 100% test coverage for new features.

Included positive and negative test cases to check edge cases.

3. Security & Session Improvements
Fixed session-related errors by properly configuring SECRET_KEY.

Enforced secure file handling using Flask’s secure_filename.

Improved authentication and session handling to prevent unauthorized access.
4. Updated UI & Documentation
Revamped HTML templates for better gallery display.

Improved Bootstrap integration for responsiveness.

Updated README.md to include API documentation and feature explanations.

Refactored project structure for better maintainability.

Running Unit Tests
Install Testing Dependencies

pip install pytest flask-testing

-This will test CRUD functionality, session management, and photo uploads.

License
This project is open-source under the MIT License.

