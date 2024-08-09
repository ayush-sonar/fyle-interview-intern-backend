# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libev-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Update pip
RUN pip install --upgrade pip

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy the bash script to the container
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Set environment variables
ENV FLASK_APP=core/server.py
ENV FLASK_ENV=production

# Expose the port the app runs on
EXPOSE 7755

# Run the bash script
CMD ["/run.sh"]