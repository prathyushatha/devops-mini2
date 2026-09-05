# DevOps Mini Project 2

## Project Overview

This project demonstrates a basic DevOps CI/CD workflow using Python,
GitHub Actions, and Docker.

Whenever new code is pushed to the GitHub repository, GitHub Actions
automatically checks the application and runs automated tests.
## 🛠️ Technologies Used

- Python
- Git
- GitHub
- GitHub Actions
- Docker
- Pytest

## 📂 Project Structure

text
devops-mini2/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── tests/
│   └── test_app.py
│
├── app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── .gitignore

Step 1: Clone the Repository

Open Command Prompt or Terminal and run:

git clone https://github.com/prathyushatha/devops-mini2.git

Then enter the project folder:

cd devops-mini2

Step 2: Install Python Dependencies

Run:
pip install -r requirements.txt
Step 3: Run the Application

Run:
python app.py

Expected output:

DevOps Mini Project 2 - Application Updated Successfully!
🧪 Run Automated Tests

The project uses Pytest for automated testing.

Run:

pytest

Expected output:

1 passed

This verifies that the application is working correctly.
