

# Instructions to build and run the Flask application using Docker

## Prerequisites

- Docker installed on your machine
- Docker Compose installed on your machine

## Dockerfile

The Dockerfile sets up the environment for the Flask application. It uses the official Python 3.10 slim image, installs necessary system dependencies, updates pip, installs Python dependencies from [`requirements.txt`]("/home/zozo/fyle-interview-intern-backend/requirements.txt"), and copies the application code and a bash script to the container.

## docker-compose.yml

The [`docker-compose.yml`]( "/home/zozo/fyle-interview-intern-backend/docker-compose.yml") file defines the services for the application. It builds the Docker image, maps port 7755 on the host to port 7755 in the container, and sets environment variables for the Flask application.

## Instructions

### Step 1: Clone the Repository

Clone the repository to your local machine:

```sh
git clone https://github.com/ayush-sonar/fyle-interview-intern-backend
cd fyle-interview-intern-backend
```
### Step 2: Convert Line Endings (Windows Only)

If you are using Windows, before building the Docker image, you need to convert the line endings of the `run.sh` file to Unix format. To do this, run the following command in the terminal:

```sh
dos2unix run.sh
```

This command ensures that the shell script can be executed correctly within the Docker container.

### Step 3: Build the Docker Image

Build the Docker image using Docker Compose:

```sh
docker-compose build
```

### Step 4: Run the Docker Container

Run the Docker container using Docker Compose:

```sh
docker-compose up
```

### Step 5: Access the Application

Open a web browser and navigate to `http://localhost:7755` to access the Flask application.

