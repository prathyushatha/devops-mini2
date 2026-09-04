# DevOps Mini Project 2

## How to Run

### Prerequisites
- Python 3.9+
- Git
- Docker (optional)

### Clone

git clone https://github.com/prathyushatha/devops-mini2.git

cd devops-mini2

### Install Dependencies

pip install -r requirements.txt

### Run Application

python app.py

Expected Output:

DevOps Mini Project 2 Running!

### Run Tests

pytest

Expected:

1 passed

### Docker

docker build -t devops-mini2 .

docker run devops-mini2

Expected:

DevOps Mini Project 2 Running!

## CI/CD

GitHub Actions automatically:
1. Checks out the code
2. Sets up Python
3. Installs dependencies
4. Runs automated tests
5. Builds the Docker image
