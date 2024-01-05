# Flask Backend Template

## Description:
Flask Backend Template is a starting point for Flask-based backend projects. Use this template to kickstart your development with a clean and organized structure for building robust web applications.


## Installation

This project is intended to run with Python 3.11, please install it via this [link](https://www.python.org/downloads/)

Install some OS packages required.

On Ubuntu:

```bash
sudo apt-get install libmagic-dev libxml2 libxslt-dev
```

Create a virtual environment if you want to install the needed packages only here (optional).

```bash
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `requirements.txt` packages.

First, install the core requirements:

```bash
pip3 install -r requirements.txt
```

## Run on Development Environment

### Using Flask Run

To run the application on the development environment, use the following command:

```bash
flask run --port 8082
```

1. Set the FLASK_APP environment variable:

```bash
export FLASK_APP=run.py
```
2. Activate the virtual environment (if created):

```bash
source venv/bin/activate
```
3. Run the Flask application:

```bash
flask run --port 8082
```
You can also set the host to 0.0.0.0 to allow access from external devices:

```bash
flask run --host=0.0.0.0 --port 8082
```
Now your Flask application will be accessible at http://localhost:8082/ or http://<your_ip>:8082/ if using --host=0.0.0.0.

### Using Docker

#### Install Docker
Ensure you have Docker installed on your machine:

- [Docker Installation Guide](https://docs.docker.com/get-docker/)

#### Build Docker Image
Build the Docker image:

```bash
docker build -t flask-backend-template .
```

#### Run the Docker container:

```bash
docker run -p 8082:5000 flask-backend-template
```

Now your Flask application will be accessible at http://localhost:8082/ or http://<your_ip>:8082/.

